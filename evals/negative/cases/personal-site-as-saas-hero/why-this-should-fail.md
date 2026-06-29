# Why This Should Fail

This fixture intentionally turns a personal portfolio and interactive toy surface into a generic SaaS landing page.

- The first viewport uses a purple/blue gradient hero and generic platform claims.
- Project, game, repo, and console routes exist only as a small dock after generic CTAs.
- The pet identity is reduced to a 36px floating button that overlaps the route dock on mobile.
- CSS has a reduced-motion media query, but the JS island keeps scheduling `requestAnimationFrame`.
- The shared island change would affect more than the homepage, but no blast-radius note is present.
