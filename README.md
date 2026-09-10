# asadullahgalib007.github.io

Personal academic website of **Asadullah Bin Rahman** — Lecturer, Department of Computer
Science and Engineering, World University of Bangladesh.

Live at <https://asadullahgalib007.github.io>.

Built with [Jekyll](https://jekyllrb.com/) on the
[al-folio](https://github.com/alshedivat/al-folio) theme (MIT), stripped down to the
pages actually in use.

## Run locally

Requires Ruby (3.2+), Bundler and ImageMagick (`convert`) for responsive images.

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

## Where the content lives

| Path                                                  | What it is                                            |
| ----------------------------------------------------- | ----------------------------------------------------- |
| `_pages/about.md`                                     | Home page — bio, education, employment                |
| `_pages/cv.md` + `_data/cv.yml`                       | CV page (PDF in `assets/pdf/Asadullah_CV.pdf`)        |
| `_pages/publications.md` + `_bibliography/papers.bib` | Publications, rendered by jekyll-scholar              |
| `_pages/teaching.md`                                  | Teaching page                                         |
| `_pages/games.md`                                     | Chess game gallery (front matter holds the game list) |
| `_news/announcement_*.md`                             | News items shown on the home page and `/news/`        |
| `_projects/` + `_pages/projects.md`                   | Projects page (not in the navbar)                     |
| `_data/coauthors.yml`                                 | Co-author name → Scholar profile links                |
| `_data/citations.yml`                                 | Citation counts, refreshed weekly by CI               |
| `_config.yml`                                         | Site settings, social links, theme options            |

`assets/json/resume.json` holds the same CV data in JSON Resume format. It is not loaded —
see the commented `jekyll_get_json` block in `_config.yml` to switch the CV page over to it.

## Automation

| Workflow                                     | Purpose                                                          |
| -------------------------------------------- | ---------------------------------------------------------------- |
| `deploy.yml`                                 | Builds the site, purges unused CSS, publishes to `gh-pages`      |
| `update-citations.yml`                       | Weekly refresh of `_data/citations.yml` via `fetch_citations.py` |
| `broken-links.yml` / `broken-links-site.yml` | Link checking on source and on the built site                    |
| `prettier.yml`                               | Formatting check                                                 |

## License

Site content © Asadullah Bin Rahman. Theme code under the MIT License — see `LICENSE`.
