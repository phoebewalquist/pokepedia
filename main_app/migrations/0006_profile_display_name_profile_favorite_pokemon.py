# Generated by Django 4.2.1 on 2023-06-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='display_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='favorite_pokemon',
            field=models.CharField(choices=[('abomasnow', 'Abomasnow'), ('abra', 'Abra'), ('absol', 'Absol'), ('accelgor', 'Accelgor'), ('aegislash', 'Aegislash'), ('aerodactyl', 'Aerodactyl'), ('aggron', 'Aggron'), ('aipom', 'Aipom'), ('alakazam', 'Alakazam'), ('alcremie', 'Alcremie'), ('alomomola', 'Alomomola'), ('altaria', 'Altaria'), ('amaura', 'Amaura'), ('ambipom', 'Ambipom'), ('amoonguss', 'Amoonguss'), ('ampharos', 'Ampharos'), ('annihilape', 'Annihilape'), ('anorith', 'Anorith'), ('appletun', 'Appletun'), ('applin', 'Applin'), ('araquanid', 'Araquanid'), ('arbok', 'Arbok'), ('arboliva', 'Arboliva'), ('arcanine', 'Arcanine'), ('arceus', 'Arceus'), ('archen', 'Archen'), ('archeops', 'Archeops'), ('arctibax', 'Arctibax'), ('arctovish', 'Arctovish'), ('arctozolt', 'Arctozolt'), ('ariados', 'Ariados'), ('armaldo', 'Armaldo'), ('armarouge', 'Armarouge'), ('aromatisse', 'Aromatisse'), ('aron', 'Aron'), ('arrokuda', 'Arrokuda'), ('articuno', 'Articuno'), ('audino', 'Audino'), ('aurorus', 'Aurorus'), ('avalugg', 'Avalugg'), ('axew', 'Axew'), ('azelf', 'Azelf'), ('azumarill', 'Azumarill'), ('azurill', 'Azurill'), ('bagon', 'Bagon'), ('baltoy', 'Baltoy'), ('banette', 'Banette'), ('barbaracle', 'Barbaracle'), ('barboach', 'Barboach'), ('barraskewda', 'Barraskewda'), ('basculegion', 'Basculegion'), ('basculin', 'Basculin'), ('bastiodon', 'Bastiodon'), ('baxcalibur', 'Baxcalibur'), ('bayleef', 'Bayleef'), ('beartic', 'Beartic'), ('beautifly', 'Beautifly'), ('beedrill', 'Beedrill'), ('beheeyem', 'Beheeyem'), ('beldum', 'Beldum'), ('bellibolt', 'Bellibolt'), ('bellossom', 'Bellossom'), ('bellsprout', 'Bellsprout'), ('bergmite', 'Bergmite'), ('bewear', 'Bewear'), ('bibarel', 'Bibarel'), ('bidoof', 'Bidoof'), ('binacle', 'Binacle'), ('bisharp', 'Bisharp'), ('blacephalon', 'Blacephalon'), ('blastoise', 'Blastoise'), ('blaziken', 'Blaziken'), ('blipbug', 'Blipbug'), ('blissey', 'Blissey'), ('blitzle', 'Blitzle'), ('boldore', 'Boldore'), ('boltund', 'Boltund'), ('bombirdier', 'Bombirdier'), ('bonsly', 'Bonsly'), ('bouffalant', 'Bouffalant'), ('bounsweet', 'Bounsweet'), ('braixen', 'Braixen'), ('brambleghast', 'Brambleghast'), ('bramblin', 'Bramblin'), ('braviary', 'Braviary'), ('breloom', 'Breloom'), ('brionne', 'Brionne'), ('bronzong', 'Bronzong'), ('bronzor', 'Bronzor'), ('brute-bonnet', 'Brute Bonnet'), ('bruxish', 'Bruxish'), ('budew', 'Budew'), ('buizel', 'Buizel'), ('bulbasaur', 'Bulbasaur'), ('buneary', 'Buneary'), ('bunnelby', 'Bunnelby'), ('burmy', 'Burmy'), ('butterfree', 'Butterfree'), ('buzzwole', 'Buzzwole'), ('cacnea', 'Cacnea'), ('cacturne', 'Cacturne'), ('calyrex', 'Calyrex'), ('camerupt', 'Camerupt'), ('capsakid', 'Capsakid'), ('carbink', 'Carbink'), ('carkol', 'Carkol'), ('carnivine', 'Carnivine'), ('carracosta', 'Carracosta'), ('carvanha', 'Carvanha'), ('cascoon', 'Cascoon'), ('castform', 'Castform'), ('caterpie', 'Caterpie'), ('celebi', 'Celebi'), ('celesteela', 'Celesteela'), ('centiskorch', 'Centiskorch'), ('ceruledge', 'Ceruledge'), ('cetitan', 'Cetitan'), ('cetoddle', 'Cetoddle'), ('chandelure', 'Chandelure'), ('chansey', 'Chansey'), ('charcadet', 'Charcadet'), ('charizard', 'Charizard'), ('charjabug', 'Charjabug'), ('charmander', 'Charmander'), ('charmeleon', 'Charmeleon'), ('chatot', 'Chatot'), ('cherrim', 'Cherrim'), ('cherubi', 'Cherubi'), ('chesnaught', 'Chesnaught'), ('chespin', 'Chespin'), ('chewtle', 'Chewtle'), ('chi-yu', 'Chi-Yu'), ('chien-pao', 'Chien-Pao'), ('chikorita', 'Chikorita'), ('chimchar', 'Chimchar'), ('chimecho', 'Chimecho'), ('chinchou', 'Chinchou'), ('chingling', 'Chingling'), ('cinccino', 'Cinccino'), ('cinderace', 'Cinderace'), ('clamperl', 'Clamperl'), ('clauncher', 'Clauncher'), ('clawitzer', 'Clawitzer'), ('claydol', 'Claydol'), ('clefable', 'Clefable'), ('clefairy', 'Clefairy'), ('cleffa', 'Cleffa'), ('clobbopus', 'Clobbopus'), ('clodsire', 'Clodsire'), ('cloyster', 'Cloyster'), ('coalossal', 'Coalossal'), ('cobalion', 'Cobalion'), ('cofagrigus', 'Cofagrigus'), ('combee', 'Combee'), ('combusken', 'Combusken'), ('comfey', 'Comfey'), ('conkeldurr', 'Conkeldurr'), ('copperajah', 'Copperajah'), ('corphish', 'Corphish'), ('corsola', 'Corsola'), ('corviknight', 'Corviknight'), ('corvisquire', 'Corvisquire'), ('cosmoem', 'Cosmoem'), ('cosmog', 'Cosmog'), ('cottonee', 'Cottonee'), ('crabominable', 'Crabominable'), ('crabrawler', 'Crabrawler'), ('cradily', 'Cradily'), ('cramorant', 'Cramorant'), ('cranidos', 'Cranidos'), ('crawdaunt', 'Crawdaunt'), ('cresselia', 'Cresselia'), ('croagunk', 'Croagunk'), ('crobat', 'Crobat'), ('crocalor', 'Crocalor'), ('croconaw', 'Croconaw'), ('crustle', 'Crustle'), ('cryogonal', 'Cryogonal'), ('cubchoo', 'Cubchoo'), ('cubone', 'Cubone'), ('cufant', 'Cufant'), ('cursola', 'Cursola'), ('cutiefly', 'Cutiefly'), ('cyclizar', 'Cyclizar'), ('cyndaquil', 'Cyndaquil'), ('dachsbun', 'Dachsbun'), ('darkrai', 'Darkrai'), ('darmanitan', 'Darmanitan'), ('dartrix', 'Dartrix'), ('darumaka', 'Darumaka'), ('decidueye', 'Decidueye'), ('dedenne', 'Dedenne'), ('deerling', 'Deerling'), ('deino', 'Deino'), ('delcatty', 'Delcatty'), ('delibird', 'Delibird'), ('delphox', 'Delphox'), ('deoxys', 'Deoxys'), ('dewgong', 'Dewgong'), ('dewott', 'Dewott'), ('dewpider', 'Dewpider'), ('dhelmise', 'Dhelmise'), ('dialga', 'Dialga'), ('diancie', 'Diancie'), ('diggersby', 'Diggersby'), ('diglett', 'Diglett'), ('ditto', 'Ditto'), ('dodrio', 'Dodrio'), ('doduo', 'Doduo'), ('dolliv', 'Dolliv'), ('dondozo', 'Dondozo'), ('donphan', 'Donphan'), ('dottler', 'Dottler'), ('doublade', 'Doublade'), ('dracovish', 'Dracovish'), ('dracozolt', 'Dracozolt'), ('dragalge', 'Dragalge'), ('dragapult', 'Dragapult'), ('dragonair', 'Dragonair'), ('dragonite', 'Dragonite'), ('drakloak', 'Drakloak'), ('drampa', 'Drampa'), ('drapion', 'Drapion'), ('dratini', 'Dratini'), ('drednaw', 'Drednaw'), ('dreepy', 'Dreepy'), ('drifblim', 'Drifblim'), ('drifloon', 'Drifloon'), ('drilbur', 'Drilbur'), ('drizzile', 'Drizzile'), ('drowzee', 'Drowzee'), ('druddigon', 'Druddigon'), ('dubwool', 'Dubwool'), ('ducklett', 'Ducklett'), ('dudunsparce', 'Dudunsparce'), ('dugtrio', 'Dugtrio'), ('dunsparce', 'Dunsparce'), ('duosion', 'Duosion'), ('duraludon', 'Duraludon'), ('durant', 'Durant'), ('dusclops', 'Dusclops'), ('dusknoir', 'Dusknoir'), ('duskull', 'Duskull'), ('dustox', 'Dustox'), ('dwebble', 'Dwebble'), ('eelektrik', 'Eelektrik'), ('eelektross', 'Eelektross'), ('eevee', 'Eevee'), ('eiscue', 'Eiscue'), ('ekans', 'Ekans'), ('eldegoss', 'Eldegoss'), ('electabuzz', 'Electabuzz'), ('electivire', 'Electivire'), ('electrike', 'Electrike'), ('electrode', 'Electrode'), ('elekid', 'Elekid'), ('elgyem', 'Elgyem'), ('emboar', 'Emboar'), ('emolga', 'Emolga'), ('empoleon', 'Empoleon'), ('enamorus', 'Enamorus'), ('entei', 'Entei'), ('escavalier', 'Escavalier'), ('espathra', 'Espathra'), ('espeon', 'Espeon'), ('espurr', 'Espurr'), ('eternatus', 'Eternatus'), ('excadrill', 'Excadrill'), ('exeggcute', 'Exeggcute'), ('exeggutor', 'Exeggutor'), ('exploud', 'Exploud'), ('falinks', 'Falinks'), ('farfetchd', "Farfetch'd"), ('farigiraf', 'Farigiraf'), ('fearow', 'Fearow'), ('feebas', 'Feebas'), ('fennekin', 'Fennekin'), ('feraligatr', 'Feraligatr'), ('ferroseed', 'Ferroseed'), ('ferrothorn', 'Ferrothorn'), ('fidough', 'Fidough'), ('finizen', 'Finizen'), ('finneon', 'Finneon'), ('flaaffy', 'Flaaffy'), ('flabebe', 'Flabébé'), ('flamigo', 'Flamigo'), ('flapple', 'Flapple'), ('flareon', 'Flareon'), ('fletchinder', 'Fletchinder'), ('fletchling', 'Fletchling'), ('flittle', 'Flittle'), ('floatzel', 'Floatzel'), ('floette', 'Floette'), ('floragato', 'Floragato'), ('florges', 'Florges'), ('flutter-mane', 'Flutter Mane'), ('flygon', 'Flygon'), ('fomantis', 'Fomantis'), ('foongus', 'Foongus'), ('forretress', 'Forretress'), ('fraxure', 'Fraxure'), ('frigibax', 'Frigibax'), ('frillish', 'Frillish'), ('froakie', 'Froakie'), ('frogadier', 'Frogadier'), ('froslass', 'Froslass'), ('frosmoth', 'Frosmoth'), ('fuecoco', 'Fuecoco'), ('furfrou', 'Furfrou'), ('furret', 'Furret'), ('gabite', 'Gabite'), ('gallade', 'Gallade'), ('galvantula', 'Galvantula'), ('garbodor', 'Garbodor'), ('garchomp', 'Garchomp'), ('gardevoir', 'Gardevoir'), ('garganacl', 'Garganacl'), ('gastly', 'Gastly'), ('gastrodon', 'Gastrodon'), ('genesect', 'Genesect'), ('gengar', 'Gengar'), ('geodude', 'Geodude'), ('gholdengo', 'Gholdengo'), ('gible', 'Gible'), ('gigalith', 'Gigalith'), ('gimmighoul', 'Gimmighoul'), ('girafarig', 'Girafarig'), ('giratina', 'Giratina'), ('glaceon', 'Glaceon'), ('glalie', 'Glalie'), ('glameow', 'Glameow'), ('glastrier', 'Glastrier'), ('gligar', 'Gligar'), ('glimmet', 'Glimmet'), ('glimmora', 'Glimmora'), ('gliscor', 'Gliscor'), ('gloom', 'Gloom'), ('gogoat', 'Gogoat'), ('golbat', 'Golbat'), ('goldeen', 'Goldeen'), ('golduck', 'Golduck'), ('golem', 'Golem'), ('golett', 'Golett'), ('golisopod', 'Golisopod'), ('golurk', 'Golurk'), ('goodra', 'Goodra'), ('goomy', 'Goomy'), ('gorebyss', 'Gorebyss'), ('gossifleur', 'Gossifleur'), ('gothita', 'Gothita'), ('gothitelle', 'Gothitelle'), ('gothorita', 'Gothorita'), ('gourgeist', 'Gourgeist'), ('grafaiai', 'Grafaiai'), ('granbull', 'Granbull'), ('grapploct', 'Grapploct'), ('graveler', 'Graveler'), ('great-tusk', 'Great Tusk'), ('greavard', 'Greavard'), ('greedent', 'Greedent'), ('greninja', 'Greninja'), ('grimer', 'Grimer'), ('grimmsnarl', 'Grimmsnarl'), ('grookey', 'Grookey'), ('grotle', 'Grotle'), ('groudon', 'Groudon'), ('grovyle', 'Grovyle'), ('growlithe', 'Growlithe'), ('grubbin', 'Grubbin'), ('grumpig', 'Grumpig'), ('gulpin', 'Gulpin'), ('gumshoos', 'Gumshoos'), ('gurdurr', 'Gurdurr'), ('guzzlord', 'Guzzlord'), ('gyarados', 'Gyarados'), ('hakamo-o', 'Hakamo-o'), ('happiny', 'Happiny'), ('hariyama', 'Hariyama'), ('hatenna', 'Hatenna'), ('hatterene', 'Hatterene'), ('hattrem', 'Hattrem'), ('haunter', 'Haunter'), ('hawlucha', 'Hawlucha'), ('haxorus', 'Haxorus'), ('heatmor', 'Heatmor'), ('heatran', 'Heatran'), ('heliolisk', 'Heliolisk'), ('helioptile', 'Helioptile'), ('heracross', 'Heracross'), ('herdier', 'Herdier'), ('hippopotas', 'Hippopotas'), ('hippowdon', 'Hippowdon'), ('hitmonchan', 'Hitmonchan'), ('hitmonlee', 'Hitmonlee'), ('hitmontop', 'Hitmontop'), ('ho-oh', 'Ho-Oh'), ('honchkrow', 'Honchkrow'), ('honedge', 'Honedge'), ('hoopa', 'Hoopa'), ('hoothoot', 'Hoothoot'), ('hoppip', 'Hoppip'), ('horsea', 'Horsea'), ('houndoom', 'Houndoom'), ('houndour', 'Houndour'), ('houndstone', 'Houndstone'), ('huntail', 'Huntail'), ('hydreigon', 'Hydreigon'), ('hypno', 'Hypno'), ('igglybuff', 'Igglybuff'), ('illumise', 'Illumise'), ('impidimp', 'Impidimp'), ('incineroar', 'Incineroar'), ('indeedee', 'Indeedee'), ('infernape', 'Infernape'), ('inkay', 'Inkay'), ('inteleon', 'Inteleon'), ('iron-bundle', 'Iron Bundle'), ('iron-hands', 'Iron Hands'), ('iron-jugulis', 'Iron Jugulis'), ('iron-leaves', 'Iron Leaves'), ('iron-moth', 'Iron Moth'), ('iron-thorns', 'Iron Thorns'), ('iron-treads', 'Iron Treads'), ('iron-valiant', 'Iron Valiant'), ('ivysaur', 'Ivysaur'), ('jangmo-o', 'Jangmo-o'), ('jellicent', 'Jellicent'), ('jigglypuff', 'Jigglypuff'), ('jirachi', 'Jirachi'), ('jolteon', 'Jolteon'), ('joltik', 'Joltik'), ('jumpluff', 'Jumpluff'), ('jynx', 'Jynx'), ('kabuto', 'Kabuto'), ('kabutops', 'Kabutops'), ('kadabra', 'Kadabra'), ('kakuna', 'Kakuna'), ('kangaskhan', 'Kangaskhan'), ('karrablast', 'Karrablast'), ('kartana', 'Kartana'), ('kecleon', 'Kecleon'), ('keldeo', 'Keldeo'), ('kilowattrel', 'Kilowattrel'), ('kingambit', 'Kingambit'), ('kingdra', 'Kingdra'), ('kingler', 'Kingler'), ('kirlia', 'Kirlia'), ('klang', 'Klang'), ('klawf', 'Klawf'), ('kleavor', 'Kleavor'), ('klefki', 'Klefki'), ('klink', 'Klink'), ('klinklang', 'Klinklang'), ('koffing', 'Koffing'), ('komala', 'Komala'), ('kommo-o', 'Kommo-o'), ('koraidon', 'Koraidon'), ('krabby', 'Krabby'), ('kricketot', 'Kricketot'), ('kricketune', 'Kricketune'), ('krokorok', 'Krokorok'), ('krookodile', 'Krookodile'), ('kubfu', 'Kubfu'), ('kyogre', 'Kyogre'), ('kyurem', 'Kyurem'), ('lairon', 'Lairon'), ('lampent', 'Lampent'), ('landorus', 'Landorus'), ('lanturn', 'Lanturn'), ('lapras', 'Lapras'), ('larvesta', 'Larvesta'), ('larvitar', 'Larvitar'), ('latias', 'Latias'), ('latios', 'Latios'), ('leafeon', 'Leafeon'), ('leavanny', 'Leavanny'), ('lechonk', 'Lechonk'), ('ledian', 'Ledian'), ('ledyba', 'Ledyba'), ('lickilicky', 'Lickilicky'), ('lickitung', 'Lickitung'), ('liepard', 'Liepard'), ('lileep', 'Lileep'), ('lilligant', 'Lilligant'), ('lillipup', 'Lillipup'), ('linoone', 'Linoone'), ('litleo', 'Litleo'), ('litten', 'Litten'), ('litwick', 'Litwick'), ('lokix', 'Lokix'), ('lombre', 'Lombre'), ('lopunny', 'Lopunny'), ('lotad', 'Lotad'), ('loudred', 'Loudred'), ('lucario', 'Lucario'), ('ludicolo', 'Ludicolo'), ('lugia', 'Lugia'), ('lumineon', 'Lumineon'), ('lunala', 'Lunala'), ('lunatone', 'Lunatone'), ('lurantis', 'Lurantis'), ('luvdisc', 'Luvdisc'), ('luxio', 'Luxio'), ('luxray', 'Luxray'), ('lycanroc', 'Lycanroc'), ('mabosstiff', 'Mabosstiff'), ('machamp', 'Machamp'), ('machoke', 'Machoke'), ('machop', 'Machop'), ('magby', 'Magby'), ('magcargo', 'Magcargo'), ('magearna', 'Magearna'), ('magikarp', 'Magikarp'), ('magmar', 'Magmar'), ('magmortar', 'Magmortar'), ('magnemite', 'Magnemite'), ('magneton', 'Magneton'), ('magnezone', 'Magnezone'), ('makuhita', 'Makuhita'), ('malamar', 'Malamar'), ('mamoswine', 'Mamoswine'), ('manaphy', 'Manaphy'), ('mandibuzz', 'Mandibuzz'), ('manectric', 'Manectric'), ('mankey', 'Mankey'), ('mantine', 'Mantine'), ('mantyke', 'Mantyke'), ('maractus', 'Maractus'), ('mareanie', 'Mareanie'), ('mareep', 'Mareep'), ('marill', 'Marill'), ('marowak', 'Marowak'), ('marshadow', 'Marshadow'), ('marshtomp', 'Marshtomp'), ('maschiff', 'Maschiff'), ('masquerain', 'Masquerain'), ('maushold', 'Maushold'), ('mawile', 'Mawile'), ('medicham', 'Medicham'), ('meditite', 'Meditite'), ('meganium', 'Meganium'), ('melmetal', 'Melmetal'), ('meloetta', 'Meloetta'), ('meltan', 'Meltan'), ('meowscarada', 'Meowscarada'), ('meowstic-male', 'Meowstic'), ('meowth', 'Meowth'), ('mesprit', 'Mesprit'), ('metagross', 'Metagross'), ('metang', 'Metang'), ('metapod', 'Metapod'), ('mew', 'Mew'), ('mewtwo', 'Mewtwo'), ('mienfoo', 'Mienfoo'), ('mienshao', 'Mienshao'), ('mightyena', 'Mightyena'), ('milcery', 'Milcery'), ('milotic', 'Milotic'), ('miltank', 'Miltank'), ('mime-jr', 'Mime Jr.'), ('mimikyu-disguised', 'Mimikyu'), ('minccino', 'Minccino'), ('minior', 'Minior'), ('minun', 'Minun'), ('miraidon', 'Miraidon'), ('misdreavus', 'Misdreavus'), ('mismagius', 'Mismagius'), ('moltres', 'Moltres'), ('monferno', 'Monferno'), ('morelull', 'Morelull'), ('morgrem', 'Morgrem'), ('morpeko', 'Morpeko'), ('mothim', 'Mothim'), ('mr-mime', 'Mr. Mime'), ('mr-rime', 'Mr. Rime'), ('mudbray', 'Mudbray'), ('mudkip', 'Mudkip'), ('mudsdale', 'Mudsdale'), ('muk', 'Muk'), ('munchlax', 'Munchlax'), ('munna', 'Munna'), ('murkrow', 'Murkrow'), ('musharna', 'Musharna'), ('nacli', 'Nacli'), ('naclstack', 'Naclstack'), ('naganadel', 'Naganadel'), ('natu', 'Natu'), ('necrozma', 'Necrozma'), ('nickit', 'Nickit'), ('nidoking', 'Nidoking'), ('nidoqueen', 'Nidoqueen'), ('nidoran-f', 'Nidoran♀'), ('nidoran-m', 'Nidoran♂'), ('nidorina', 'Nidorina'), ('nidorino', 'Nidorino'), ('nihilego', 'Nihilego'), ('nincada', 'Nincada'), ('ninetales', 'Ninetales'), ('ninjask', 'Ninjask'), ('noctowl', 'Noctowl'), ('noibat', 'Noibat'), ('noivern', 'Noivern'), ('nosepass', 'Nosepass'), ('numel', 'Numel'), ('nuzleaf', 'Nuzleaf'), ('nymble', 'Nymble'), ('obstagoon', 'Obstagoon'), ('octillery', 'Octillery'), ('oddish', 'Oddish'), ('oinkologne', 'Oinkologne'), ('omanyte', 'Omanyte'), ('omastar', 'Omastar'), ('onix', 'Onix'), ('oranguru', 'Oranguru'), ('orbeetle', 'Orbeetle'), ('oricorio', 'Oricorio'), ('orthworm', 'Orthworm'), ('oshawott', 'Oshawott'), ('overqwil', 'Overqwil'), ('pachirisu', 'Pachirisu'), ('palafin', 'Palafin'), ('palkia', 'Palkia'), ('palossand', 'Palossand'), ('palpitoad', 'Palpitoad'), ('pancham', 'Pancham'), ('pangoro', 'Pangoro'), ('panpour', 'Panpour'), ('pansage', 'Pansage'), ('pansear', 'Pansear'), ('paras', 'Paras'), ('parasect', 'Parasect'), ('passimian', 'Passimian'), ('patrat', 'Patrat'), ('pawmi', 'Pawmi'), ('pawmo', 'Pawmo'), ('pawmot', 'Pawmot'), ('pawniard', 'Pawniard'), ('pelipper', 'Pelipper'), ('perrserker', 'Perrserker'), ('persian', 'Persian'), ('petilil', 'Petilil'), ('phanpy', 'Phanpy'), ('phantump', 'Phantump'), ('pheromosa', 'Pheromosa'), ('phione', 'Phione'), ('pichu', 'Pichu'), ('pidgeot', 'Pidgeot'), ('pidgeotto', 'Pidgeotto'), ('pidgey', 'Pidgey'), ('pidove', 'Pidove'), ('pignite', 'Pignite'), ('pikachu', 'Pikachu'), ('pikipek', 'Pikipek'), ('piloswine', 'Piloswine'), ('pincurchin', 'Pincurchin'), ('pineco', 'Pineco'), ('pinsir', 'Pinsir'), ('piplup', 'Piplup'), ('plusle', 'Plusle'), ('poipole', 'Poipole'), ('politoed', 'Politoed'), ('poliwag', 'Poliwag'), ('poliwhirl', 'Poliwhirl'), ('poliwrath', 'Poliwrath'), ('polteageist', 'Polteageist'), ('ponyta', 'Ponyta'), ('poochyena', 'Poochyena'), ('popplio', 'Popplio'), ('porygon', 'Porygon'), ('porygon-z', 'Porygon-Z'), ('porygon2', 'Porygon2'), ('primarina', 'Primarina'), ('primeape', 'Primeape'), ('prinplup', 'Prinplup'), ('probopass', 'Probopass'), ('psyduck', 'Psyduck'), ('pumpkaboo', 'Pumpkaboo'), ('pupitar', 'Pupitar'), ('purrloin', 'Purrloin'), ('purugly', 'Purugly'), ('pyroar', 'Pyroar'), ('pyukumuku', 'Pyukumuku'), ('quagsire', 'Quagsire'), ('quaquaval', 'Quaquaval'), ('quaxly', 'Quaxly'), ('quaxwell', 'Quaxwell'), ('quilava', 'Quilava'), ('quilladin', 'Quilladin'), ('qwilfish', 'Qwilfish'), ('raboot', 'Raboot'), ('rabsca', 'Rabsca'), ('raichu', 'Raichu'), ('raikou', 'Raikou'), ('ralts', 'Ralts'), ('rampardos', 'Rampardos'), ('rapidash', 'Rapidash'), ('raticate', 'Raticate'), ('rattata', 'Rattata'), ('rayquaza', 'Rayquaza'), ('regice', 'Regice'), ('regidrago', 'Regidrago'), ('regieleki', 'Regieleki'), ('regigigas', 'Regigigas'), ('regirock', 'Regirock'), ('registeel', 'Registeel'), ('relicanth', 'Relicanth'), ('rellor', 'Rellor'), ('remoraid', 'Remoraid'), ('reshiram', 'Reshiram'), ('reuniclus', 'Reuniclus'), ('revavroom', 'Revavroom'), ('rhydon', 'Rhydon'), ('rhyhorn', 'Rhyhorn'), ('rhyperior', 'Rhyperior'), ('ribombee', 'Ribombee'), ('rillaboom', 'Rillaboom'), ('riolu', 'Riolu'), ('roaring-moon', 'Roaring Moon'), ('rockruff', 'Rockruff'), ('roggenrola', 'Roggenrola'), ('rolycoly', 'Rolycoly'), ('rookidee', 'Rookidee'), ('roselia', 'Roselia'), ('roserade', 'Roserade'), ('rotom', 'Rotom'), ('rowlet', 'Rowlet'), ('rufflet', 'Rufflet'), ('runerigus', 'Runerigus'), ('sableye', 'Sableye'), ('salamence', 'Salamence'), ('salandit', 'Salandit'), ('salazzle', 'Salazzle'), ('samurott', 'Samurott'), ('sandaconda', 'Sandaconda'), ('sandile', 'Sandile'), ('sandshrew', 'Sandshrew'), ('sandslash', 'Sandslash'), ('sandy-shocks', 'Sandy Shocks'), ('sandygast', 'Sandygast'), ('sawk', 'Sawk'), ('sawsbuck', 'Sawsbuck'), ('scatterbug', 'Scatterbug'), ('sceptile', 'Sceptile'), ('scizor', 'Scizor'), ('scolipede', 'Scolipede'), ('scorbunny', 'Scorbunny'), ('scovillain', 'Scovillain'), ('scrafty', 'Scrafty'), ('scraggy', 'Scraggy'), ('scream-tail', 'Scream Tail'), ('scyther', 'Scyther'), ('seadra', 'Seadra'), ('seaking', 'Seaking'), ('sealeo', 'Sealeo'), ('seedot', 'Seedot'), ('seel', 'Seel'), ('seismitoad', 'Seismitoad'), ('sentret', 'Sentret'), ('serperior', 'Serperior'), ('servine', 'Servine'), ('seviper', 'Seviper'), ('sewaddle', 'Sewaddle'), ('sharpedo', 'Sharpedo'), ('shaymin', 'Shaymin'), ('shedinja', 'Shedinja'), ('shelgon', 'Shelgon'), ('shellder', 'Shellder'), ('shellos', 'Shellos'), ('shelmet', 'Shelmet'), ('shieldon', 'Shieldon'), ('shiftry', 'Shiftry'), ('shiinotic', 'Shiinotic'), ('shinx', 'Shinx'), ('shroodle', 'Shroodle'), ('shroomish', 'Shroomish'), ('shuckle', 'Shuckle'), ('shuppet', 'Shuppet'), ('sigilyph', 'Sigilyph'), ('silcoon', 'Silcoon'), ('silicobra', 'Silicobra'), ('silvally', 'Silvally'), ('simipour', 'Simipour'), ('simisage', 'Simisage'), ('simisear', 'Simisear'), ('sinistea', 'Sinistea'), ('sirfetchd', "Sirfetch'd"), ('sizzlipede', 'Sizzlipede'), ('skarmory', 'Skarmory'), ('skeledirge', 'Skeledirge'), ('skiddo', 'Skiddo'), ('skiploom', 'Skiploom'), ('skitty', 'Skitty'), ('skorupi', 'Skorupi'), ('skrelp', 'Skrelp'), ('skuntank', 'Skuntank'), ('skwovet', 'Skwovet'), ('slaking', 'Slaking'), ('slakoth', 'Slakoth'), ('sliggoo', 'Sliggoo'), ('slither-wing', 'Slither Wing'), ('slowbro', 'Slowbro'), ('slowking', 'Slowking'), ('slowpoke', 'Slowpoke'), ('slugma', 'Slugma'), ('slurpuff', 'Slurpuff'), ('smeargle', 'Smeargle'), ('smoliv', 'Smoliv'), ('smoochum', 'Smoochum'), ('sneasel', 'Sneasel'), ('sneasler', 'Sneasler'), ('snivy', 'Snivy'), ('snom', 'Snom'), ('snorlax', 'Snorlax'), ('snorunt', 'Snorunt'), ('snover', 'Snover'), ('snubbull', 'Snubbull'), ('sobble', 'Sobble'), ('solgaleo', 'Solgaleo'), ('solosis', 'Solosis'), ('solrock', 'Solrock'), ('spearow', 'Spearow'), ('spectrier', 'Spectrier'), ('spewpa', 'Spewpa'), ('spheal', 'Spheal'), ('spidops', 'Spidops'), ('spinarak', 'Spinarak'), ('spinda', 'Spinda'), ('spiritomb', 'Spiritomb'), ('spoink', 'Spoink'), ('sprigatito', 'Sprigatito'), ('spritzee', 'Spritzee'), ('squawkabilly', 'Squawkabilly'), ('squirtle', 'Squirtle'), ('stakataka', 'Stakataka'), ('stantler', 'Stantler'), ('staraptor', 'Staraptor'), ('staravia', 'Staravia'), ('starly', 'Starly'), ('starmie', 'Starmie'), ('staryu', 'Staryu'), ('steelix', 'Steelix'), ('steenee', 'Steenee'), ('stonjourner', 'Stonjourner'), ('stoutland', 'Stoutland'), ('stufful', 'Stufful'), ('stunfisk', 'Stunfisk'), ('stunky', 'Stunky'), ('sudowoodo', 'Sudowoodo'), ('suicune', 'Suicune'), ('sunflora', 'Sunflora'), ('sunkern', 'Sunkern'), ('surskit', 'Surskit'), ('swablu', 'Swablu'), ('swadloon', 'Swadloon'), ('swalot', 'Swalot'), ('swampert', 'Swampert'), ('swanna', 'Swanna'), ('swellow', 'Swellow'), ('swinub', 'Swinub'), ('swirlix', 'Swirlix'), ('swoobat', 'Swoobat'), ('sylveon', 'Sylveon'), ('tadbulb', 'Tadbulb'), ('taillow', 'Taillow'), ('talonflame', 'Talonflame'), ('tandemaus', 'Tandemaus'), ('tangela', 'Tangela'), ('tangrowth', 'Tangrowth'), ('tapu-bulu', 'Tapu Bulu'), ('tapu-fini', 'Tapu Fini'), ('tapu-koko', 'Tapu Koko'), ('tapu-lele', 'Tapu Lele'), ('tarountula', 'Tarountula'), ('tatsugiri', 'Tatsugiri'), ('tauros', 'Tauros'), ('teddiursa', 'Teddiursa'), ('tentacool', 'Tentacool'), ('tentacruel', 'Tentacruel'), ('tepig', 'Tepig'), ('terrakion', 'Terrakion'), ('thievul', 'Thievul'), ('throh', 'Throh'), ('thundurus', 'Thundurus'), ('thwackey', 'Thwackey'), ('timburr', 'Timburr'), ('ting-lu', 'Ting-Lu'), ('tinkatink', 'Tinkatink'), ('tinkaton', 'Tinkaton'), ('tinkatuff', 'Tinkatuff'), ('tirtouga', 'Tirtouga'), ('toedscool', 'Toedscool'), ('toedscruel', 'Toedscruel'), ('togedemaru', 'Togedemaru'), ('togekiss', 'Togekiss'), ('togepi', 'Togepi'), ('togetic', 'Togetic'), ('torchic', 'Torchic'), ('torkoal', 'Torkoal'), ('tornadus', 'Tornadus'), ('torracat', 'Torracat'), ('torterra', 'Torterra'), ('totodile', 'Totodile'), ('toucannon', 'Toucannon'), ('toxapex', 'Toxapex'), ('toxel', 'Toxel'), ('toxicroak', 'Toxicroak'), ('toxtricity', 'Toxtricity'), ('tranquill', 'Tranquill'), ('trapinch', 'Trapinch'), ('treecko', 'Treecko'), ('trevenant', 'Trevenant'), ('tropius', 'Tropius'), ('trubbish', 'Trubbish'), ('trumbeak', 'Trumbeak'), ('tsareena', 'Tsareena'), ('turtonator', 'Turtonator'), ('turtwig', 'Turtwig'), ('tympole', 'Tympole'), ('tynamo', 'Tynamo'), ('type-null', 'Type: Null'), ('typhlosion', 'Typhlosion'), ('tyranitar', 'Tyranitar'), ('tyrantrum', 'Tyrantrum'), ('tyrogue', 'Tyrogue'), ('tyrunt', 'Tyrunt'), ('umbreon', 'Umbreon'), ('unfezant', 'Unfezant'), ('unown', 'Unown'), ('ursaluna', 'Ursaluna'), ('ursaring', 'Ursaring'), ('urshifu', 'Urshifu'), ('uxie', 'Uxie'), ('vanillish', 'Vanillish'), ('vanillite', 'Vanillite'), ('vanilluxe', 'Vanilluxe'), ('vaporeon', 'Vaporeon'), ('varoom', 'Varoom'), ('veluza', 'Veluza'), ('venipede', 'Venipede'), ('venomoth', 'Venomoth'), ('venonat', 'Venonat'), ('venusaur', 'Venusaur'), ('vespiquen', 'Vespiquen'), ('vibrava', 'Vibrava'), ('victini', 'Victini'), ('victreebel', 'Victreebel'), ('vigoroth', 'Vigoroth'), ('vikavolt', 'Vikavolt'), ('vileplume', 'Vileplume'), ('virizion', 'Virizion'), ('vivillon', 'Vivillon'), ('volbeat', 'Volbeat'), ('volcanion', 'Volcanion'), ('volcarona', 'Volcarona'), ('voltorb', 'Voltorb'), ('vullaby', 'Vullaby'), ('vulpix', 'Vulpix'), ('wailmer', 'Wailmer'), ('wailord', 'Wailord'), ('walking-wake', 'Walking Wake'), ('walrein', 'Walrein'), ('wartortle', 'Wartortle'), ('watchog', 'Watchog'), ('wattrel', 'Wattrel'), ('weavile', 'Weavile'), ('weedle', 'Weedle'), ('weepinbell', 'Weepinbell'), ('weezing', 'Weezing'), ('whimsicott', 'Whimsicott'), ('whirlipede', 'Whirlipede'), ('whiscash', 'Whiscash'), ('whismur', 'Whismur'), ('wigglytuff', 'Wigglytuff'), ('wiglett', 'Wiglett'), ('wimpod', 'Wimpod'), ('wingull', 'Wingull'), ('wishiwashi', 'Wishiwashi'), ('wo-chien', 'Wo-Chien'), ('wobbuffet', 'Wobbuffet'), ('woobat', 'Woobat'), ('wooloo', 'Wooloo'), ('wooper', 'Wooper'), ('wormadam', 'Wormadam'), ('wugtrio', 'Wugtrio'), ('wurmple', 'Wurmple'), ('wynaut', 'Wynaut'), ('wyrdeer', 'Wyrdeer'), ('xatu', 'Xatu'), ('xerneas', 'Xerneas'), ('xurkitree', 'Xurkitree'), ('yamask', 'Yamask'), ('yamper', 'Yamper'), ('yanma', 'Yanma'), ('yanmega', 'Yanmega'), ('yungoos', 'Yungoos'), ('yveltal', 'Yveltal'), ('zacian', 'Zacian'), ('zamazenta', 'Zamazenta'), ('zangoose', 'Zangoose'), ('zapdos', 'Zapdos'), ('zarude', 'Zarude'), ('zebstrika', 'Zebstrika'), ('zekrom', 'Zekrom'), ('zeraora', 'Zeraora'), ('zigzagoon', 'Zigzagoon'), ('zoroark', 'Zoroark'), ('zorua', 'Zorua'), ('zubat', 'Zubat'), ('zweilous', 'Zweilous'), ('zygarde', 'Zygarde')], default='Slowpoke', max_length=100),
        ),
    ]
