import requests;
import random;

def main():
    main_skill = None
    while main_skill == None:
        main_skill = get_random_skill_gem()

# Query for getting all the active spells
# Currently there are 429 skill gems in Settlers League
def get_skill_gems():
    res = requests.get('https://pathofexile.fandom.com/api.php?action=cargoquery&tables=skill&limit=500&fields=active_skill_name,description,item_class_id_restriction,item_class_restriction,stat_text&group_by=active_skill_name&format=json');
    data = res.json()['cargoquery']; # Returns array of founds skill gems
    return data

# Get random main skill gem
def get_random_skill_gem():
    skill_gems = get_skill_gems()
    random_main = random.choice(skill_gems)
    random_main = random_main['title']
    # Condition for none type
    if random_main is None:
        return None

    # Check stat text if spell does damage..
    stat_text = random_main['stat text']
    if stat_text is None:
        return None

    if not ('deals' in stat_text or 'leeches' in stat_text or 'deal' in stat_text or 'deals' in stat_text and 'damage' in stat_text or 'summons' in stat_text or 'summon' in stat_text):
        return None
    # Conditions for when we get a spell that for sure wont work

    # One of the conditions should be that does the spell deal or reflect damage in any way...

    # Other condition should compare if the skill is in the list of skills you can only get from the old labyrinth 
    print(random_main)
    return random_main

# Query for getting all the support gems depending on the main damage attribute of the main skill
# Needs to be ran enough times to form a 6 link, that can function in the actual game.


main()