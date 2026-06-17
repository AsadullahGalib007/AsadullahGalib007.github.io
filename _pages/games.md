---
layout: page
title: "Games"
permalink: /games/
nav: true
nav_order: 7

# Each board preview is the *final* position of the game (the moment it was won).
# Click "replay" on a card to load the full interactive Lichess board.
games:
  - id: YHiFxq9U
    color: White
    opponent: gallitoss
    opp_rating: 1505
    my_rating: 1376
    result: Checkmate
    opening: "Four Knights Game: Italian Variation"
    eco: C47
    date: "Jun 18, 2024"
    upset: 129
  - id: pwtX9Bj8
    color: White
    opponent: Vladimir_9174
    opp_rating: 1492
    my_rating: 1404
    result: Resignation
    opening: "Four Knights Game: Italian Variation"
    eco: C47
    date: "Sep 30, 2024"
    upset: 88
  - id: SCNUTLTh
    color: White
    opponent: tomatillo97
    opp_rating: 1517
    my_rating: 1498
    result: Checkmate
    opening: "Italian Game: Giuoco Pianissimo"
    eco: C50
    date: "Oct 10, 2024"
    anchor: "#61"
  - id: rncRaNIh
    color: White
    opponent: Auxius
    opp_rating: 1508
    my_rating: 1502
    result: Checkmate
    opening: "Italian Game: Giuoco Pianissimo"
    eco: C50
    date: "Oct 11, 2024"
    anchor: "#49"
  - id: wRwL7iBr
    color: Black
    opponent: paromapa
    opp_rating: 1481
    my_rating: 1483
    result: Checkmate
    opening: "Italian Game: Scotch Invitation Declined"
    eco: C56
    date: "Oct 4, 2024"
  - id: w45dtccK
    color: White
    opponent: zeyadal7arthi
    opp_rating: 1476
    my_rating: 1454
    result: Checkmate
    opening: "Four Knights Game: Italian Variation"
    eco: C47
    date: "Oct 6, 2024"
  - id: jxilWcoQ
    color: White
    opponent: Efnvhbft
    opp_rating: 1429
    my_rating: 1459
    result: Checkmate
    opening: "Four Knights Game: Italian Variation"
    eco: C47
    date: "Oct 3, 2024"
---

## My Chess Games

I am no chess master — this is just where I unwind. These aren't my whole record, just a handful of games I had fun playing and felt were worth sharing. Each card shows the **final position**; hit replay to step through the whole game. Care for a match? Challenge me on [Lichess](https://lichess.org/?user=AsadullahGalib#friend).

<div class="chess-stats">
  <div class="chess-stat"><span class="num">{{ page.games | size }}</span><span class="label">Featured games</span></div>
  <div class="chess-stat"><span class="num">1517</span><span class="label">Toughest foe</span></div>
  <div class="chess-stat"><span class="num">+129</span><span class="label">Biggest upset</span></div>
</div>

<div class="chess-gallery">
  {% for game in page.games %}
  <div class="chess-card">
    <div class="chess-card__board">
      <img loading="lazy" src="https://lichess1.org/game/export/gif/thumbnail/{{ game.id }}.gif" alt="Final position of my game versus {{ game.opponent }}" />
      <span class="chess-card__badge">♚ WIN</span>
      {% if game.upset %}<span class="chess-card__upset">⚡ +{{ game.upset }}</span>{% endif %}
      <button class="chess-card__play" type="button" aria-label="Replay game versus {{ game.opponent }}" data-embed="https://lichess.org/embed/game/{{ game.id }}?theme=auto&bg=auto{{ game.anchor }}">▶</button>
    </div>
    <div class="chess-card__body">
      <div class="chess-card__opponent">vs {{ game.opponent }} <span class="rating">({{ game.opp_rating }})</span></div>
      <div class="chess-card__opening">{{ game.eco }} · {{ game.opening }}</div>
      <div class="chess-card__meta">
        <span>I played {{ game.color }}</span>
        <span>{{ game.result }}</span>
        <span>{{ game.date }}</span>
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<div class="chess-modal" id="chessModal" hidden>
  <div class="chess-modal__backdrop" data-close></div>
  <div class="chess-modal__dialog" role="dialog" aria-modal="true" aria-label="Game replay">
    <button class="chess-modal__close" type="button" data-close aria-label="Close replay">×</button>
    <div class="chess-modal__body"></div>
  </div>
</div>

<script>
  (function () {
    var modal = document.getElementById("chessModal");
    var body = modal.querySelector(".chess-modal__body");

    // Size the embed so the whole stacked layout fits with no dark gutter:
    // board (= dialog width) + player rows (2 x 2em) + controls (4em) +
    // moves (6em) = width + 14em, at the embed's responsive root font-size.
    // Keeping the width <= 440px holds Lichess in that stacked layout.
    function open(src) {
      var w = Math.min(440, Math.floor(window.innerWidth * 0.92));
      var fontPx = Math.min(19, Math.max(12, 12 + (2 * (w - 300)) / 900));
      var h = Math.min(Math.ceil(w + 14 * fontPx), Math.floor(window.innerHeight * 0.9));

      var frame = document.createElement("iframe");
      frame.src = src;
      frame.setAttribute("allowfullscreen", "");
      frame.style.height = h + "px";

      body.innerHTML = "";
      body.appendChild(frame);
      modal.hidden = false;
      document.body.style.overflow = "hidden";
    }

    function close() {
      modal.hidden = true;
      body.innerHTML = ""; // stop the embed / free the iframe
      document.body.style.overflow = "";
    }

    document.querySelectorAll(".chess-card__play").forEach(function (btn) {
      btn.addEventListener("click", function () {
        open(btn.getAttribute("data-embed"));
      });
    });
    modal.addEventListener("click", function (e) {
      if (e.target.hasAttribute("data-close")) close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !modal.hidden) close();
    });
  })();
</script>
