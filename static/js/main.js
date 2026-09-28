(function () {
  var vids = document.querySelectorAll('video[data-autoplay]');
  function play(v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  var hoverable = window.matchMedia('(hover: hover)').matches;
  if ('IntersectionObserver' in window && vids.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { if (!hoverable || v.closest('.prose, .project-hero')) play(v); }
        else { v.pause(); }
      });
    }, { rootMargin: '120px 0px', threshold: 0.1 });
    vids.forEach(function (v) { io.observe(v); });
  } else {
    vids.forEach(function (v) { v.setAttribute('autoplay', ''); });
  }
  // Tiles: poster first, play on hover (desktop) or when scrolled into view (touch).
  if (hoverable) {
    document.querySelectorAll('.tile').forEach(function (t) {
      var v = t.querySelector('video[data-autoplay]'); if (!v) return;
      t.addEventListener('mouseenter', function () { play(v); });
      t.addEventListener('mouseleave', function () { v.pause(); });
    });
  }
})();
