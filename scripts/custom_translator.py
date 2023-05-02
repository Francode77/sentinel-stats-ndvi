## Custom translator function for English users

def translate_to_ENG(df_agri):
    df_agri.rename(columns={"GEWASGROEP": "CROP_TYPE", "LENGTE": "LENGTH", "OPPERVL" : "SURF_AREA"},inplace=True)

    categories = df_agri['CROP_TYPE']

    # Create a dictionary to map each Dutch term to its English translation
    translations = {
        'Maïs': 'Corn',
        'Overige gewassen': 'Other crops',
        'Houtachtige gewassen': 'Woody crops',
        'Grasland': 'Grassland',
        'Groenten, kruiden en sierplanten': 'Vegetables, herbs, and ornamental plants',
        'Water': 'Water',
        'Fruit en Noten': 'Fruit and nuts',
        'Granen, zaden en peulvruchten': 'Cereals, seeds, and legumes',
        'Voedergewassen': 'Forage crops',
        'Aardappelen': 'Potatoes',
        'Suikerbieten': 'Sugar beets',
        'Vlas en hennep': 'Flax and hemp',
        'Landbouwinfrastructuur': 'Agricultural infrastructure'
    }

    # Replace the Dutch terms in the 'CROP_TYPE' column with their English translations
    df_agri['CROP_TYPE'] = df_agri['CROP_TYPE'].replace(translations)

    translations = {
    'Silomaïs': 'Silage corn',
    'Niet nader omschreven gewas - kleine landbouwer': 'Unspecified crop - small farmer',
    'Houtkanten en houtwallen <= 10 m breed': 'Hedgerows and woodlots <= 10 m wide',
    'Korrelmaïs': 'Grain corn',
    'Natuurlijk grasland met minimumactiviteit': 'Natural grassland with minimal activity',
    'Grasland': 'Grassland',
    'Asperges - vers': 'Asparagus - fresh',
    'Poelen <= 0,1 ha': 'Ponds <= 0.1 ha',
    'Graskruiden mengsel': 'Grass and herb mixture',
    'Meerjarige fruitteelten (peer)': 'Perennial fruit crops (pear)',
    'Faunamengsel': 'Wildlife mixture',
    'Bloemenmengsel': 'Flower mixture',
    'Grasklaver': 'Grass and clover',
    'Weiland met niet-oogstbare bomen (> 100 bomen per ha)': 'Pasture with non-harvestable trees (> 100 trees per ha)',
    'Kerstbomen': 'Christmas trees',
    'Wintertarwe': 'Winter wheat',
    'Voederbieten': 'Fodder beets',
    'Aardappelen (geplande oogst voor 1/9)': 'Potatoes (planned harvest before 1/9)',
    'Aardappelen (geplande oogst vanaf 1/9)': 'Potatoes (planned harvest from 1/9)',
    'Ajuinen (niet-vroege) - industrie': 'Onions (non-early) - industry',
    'Winterrogge': 'Winter rye',
    'Zaaizaad grassen': 'Grass seed',
    'Tuin- en veldbonen (Vicia faba) - industrie': 'Garden and field beans (Vicia faba) - industry',
    'Suikerbieten': 'Sugar beets',
    'Wintergerst': 'Winter barley',
    'Zomergerst': 'Spring barley',
    'Vezelvlas (bestemd voor vezelproductie)': 'Flax for fiber production',
    'Cichorei (inuline)': 'Chicory (inulin)',
    'Braakliggend land zonder minimale activiteit': 'Fallow land with no minimum activity',
    'Ajuinen (niet vroege) - vers': 'Onions (non-early) - fresh',
    'Spelt': 'Spelt',
    'Wortel (vroege) (consumptie) - industrie': 'Carrots (early) (consumption) - industry',
    'Zomerhaver': 'Spring oats',
    'Triticale': 'Triticale',
    'Niet nader omschreven gebouw': 'Unspecified building',
    'Ajuinen (vroege) - industrie': 'Onions (early) - industry',
    'Quinoa': 'Quinoa',
    'Loods (bv. voor machines, opslag,?)': 'Shed (e.g. for machinery, storage, etc.)',
    'Ajuinen (vroege) - vers': 'Onions (early) - fresh',
    'Bloemkool - vers': 'Cauliflower - fresh',
    'Boomkweek - bos- en haagplanten': 'Tree nursery - forest and hedge plants',
    'Meerjarige fruitteelten (appel)': 'Perennial fruit crops (apple)',
    'Stal': 'Stable',
    'Woonhuis': 'Residential house',
    'Ander gebouw': 'Other building',
    'Gebouw i.k.v. verbreding': 'Building in the context of diversification',
    'Snijrogge': 'Winter rye for silage',
    'Sojabonen': 'Soybeans'
    }

    # Replace the Dutch terms in the 'GEWASGROEP' column with their English translations
    df_agri['LBLHFDTLT'] = df_agri['LBLHFDTLT'].replace(translations)

    translations = { 
    'Maaien met afvoer': 'Mowing with removal',
    'Blijvend grasland gescheurd': 'Perennial grassland plowed'
    }
    # Replace the Dutch terms in the 'GEWASGROEP' column with their English translations
    df_agri['LBLPM'] = df_agri['LBLPM'].replace(translations)

    return df_agri
 