from pathlib import Path
s=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_surface():
 for n in ['set_table','plate_component','get_table','get_tastings_page','get_tables_page','get_summary']:assert f'def {n}' in s
def test_guards():
 for n in ['actor in cooks','role in plates','len(plates)==len(roles)','int(t.burns)>=3','run_nondet_unsafe']:assert n in s
