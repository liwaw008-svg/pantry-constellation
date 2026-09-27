# Pantry Constellation

`SERVICE: TABLE WAITING FOR A COMPLETE MEAL`

## Pantry inventory

A host records diners, dietary rules, available ingredients, and the roles a meal must fill. Each wallet cooks once. The authoritative pantry and every accepted plate live in one GenLayer contract; the static Next.js kitchen reads and writes through `genlayer-js`.

## Plating law

`set_table` freezes the service. `plate_component` accepts an open role, dish name, and preparation method. Before consensus, code blocks duplicate cooks, filled roles, closed tables, and thin methods. Validators independently check ingredient availability, every dietary rule, role fit, and compatibility with plated food. Code plates a feasible component or burns one of three timer tokens. All roles produce `SERVED`; three burns produce `CLOSED`.

Paged tasting and table views, plus `get_table` and `get_summary`, feed the radial kitchen without one-call-per-item loops. GenLayer is essential because substitution and meal compatibility are contextual, yet no host should unilaterally decide the shared menu.

## Kitchen setup

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
cd frontend
npm install
npm run typecheck
npm run build
```

The overhead prep table uses orbiting pantry jars, plate wells, timer motion, paper grain, and a continuous cook counter. It does not order groceries, provide medical nutrition advice, certify allergen safety, or move funds.

## Leftovers

- Contract: `0x75ec16dfCb49A3d99bC8F11e3f984762bcC5ad92`
- Deployment: `0x08dcfe936ba7ec6c3cb510df613f6fa46d49f41b14bce8bffa81c32ab7520dc1`
- Repository: https://github.com/liwaw008-svg/pantry-constellation
- Public kitchen: https://liwaw008-svg-pantry-constellation.pages.dev/
