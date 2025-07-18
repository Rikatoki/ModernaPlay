def jogos_json():
    with open('app/data/jogos.json', 'r') as f:
        from json import load
        return load(f)