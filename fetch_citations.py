import requests
import yaml
import time
import os

papers = [
    {"key": "rahman2025systematicevaluationwaveletbaseddenoising", "id": "ARXIV:2508.15011"},
    {"key": "rahman2025deeplearningarchitecturesmedical", "id": "ARXIV:2508.17223"},
    {"key": "11013062", "id": "DOI:10.1109/ECCE64574.2025.11013062"},
    {"key": "10441064", "id": "DOI:10.1109/ICCIT60459.2023.10441064"}
]

citations_data = {}
print("Fetching citation counts from Semantic Scholar...")

for paper in papers:
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper['id']}?fields=citationCount,title"
    
    # Retry logic for rate limits (429)
    for attempt in range(3):
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                count = data.get('citationCount', 0)
                citations_data[paper['key']] = count
                print(f"✅ {paper['key']}: {count} citations")
                break # Success, exit retry loop
            elif response.status_code == 429:
                wait_time = 3 * (attempt + 1)
                print(f"⏳ {paper['key']}: Rate limited (429). Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            elif response.status_code == 404:
                print(f"⚠️ {paper['key']}: Not found in Semantic Scholar. Setting to 0.")
                citations_data[paper['key']] = 0
                break
            else:
                print(f"❌ {paper['key']}: Failed (Status {response.status_code})")
                citations_data[paper['key']] = 0
                break
                
        except Exception as e:
            print(f"❌ Error fetching {paper['key']}: {e}")
            citations_data[paper['key']] = 0
            break
            
    # Wait 1.5 seconds between papers to avoid hitting the rate limit in the first place
    time.sleep(1.5) 

# Save the results to _data/citations.yml
os.makedirs('_data', exist_ok=True)
with open('_data/citations.yml', 'w') as f:
    yaml.dump(citations_data, f, default_flow_style=False)

print("\n✅ Success! Citations saved to _data/citations.yml")