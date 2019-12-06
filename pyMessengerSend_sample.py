# apt install python
# apt install pip3
# pip3 fbchat

# python3 pyMessengerSend.py
# -t : Test sans appeler l'API
# -d : "destinataires" (séparés pas des espaces)
# -m : "message"
# -n : nombre de messages par personne
# -w : intervalle de temps entre message
# -p : type de phrase

from fbchat import Client
from fbchat.models import Message, MessageReaction
import sys, random, time

username = "email"
password = "password"
if not "-t" in sys.argv: client = Client(username, password)

friends = {
	'pseudo' : {
		'ID' : 123456789098,
		'CN' : 'prenom.nom'
	}
}
phrases = {
	'culte' : {
		'Ok, jvais l\'refaire ...',
		'Bon, maintenant je vais me repository',
		'Depuis longtemps ...',
		'Ah ben, je C pas !',
		'Ah ben maintenant j\'ai un postfix',
		'TRACE !!!'
	},
	'où' : {
		'mon' : {
			'communs' : [
				'slack',
				'where1',
				'amplifieur de mauvaise qualité',
				'caissier'
			],
			'noms' : [
				'Absolon',
				'Achille',
				'Adolphe',
				'Adrien',
				'Alain',
				'Alexandre',
				'Alphonse',
				'Amaury',
				'Ambroise',
				'Anatole',
				'Anselme',
				'Antoine',
				'Apollinaire',
				'Aristide',
				'Armand',
				'Armel',
				'Arnaud',
				'Auguste',
				'Augustin',
				'Aurelien',
				'Baptiste',
				'Basile',
				'Bastien',
				'Baudouin',
				'Benoit',
				'Bertrand',
				'Blaise',
				'Brice',
				'Cesaire',
				'Charlot',
				'Christophe',
				'Colombain',
				'Constantin',
				'Corin',
				'Damien',
				'Denis',
				'Didier',
				'Diodore',
				'Dion',
				'Donatien',
				'Edgard',
				'Edmond',
				'Eloi',
				'Ermenegilde',
				'Eustache',
				'Evrard',
				'Fabien',
				'Fabrice',
				'Felicien',
				'Fernand',
				'Fiacre',
				'Firmin',
				'Florentin',
				'Franck',
				'Gaspard',
				'Gaston',
				'Gautier',
				'Geoffroi',
				'Georges',
				'Germain',
				'Gervais',
				'Ghislain',
				'Gilles',
				'Godelieve',
				'Gratien',
				'Guillaume',
				'Gustave',
				'Henri',
				'Hercule',
				'Hilaire',
				'Hugues',
				'Ignace',
				'Jacques',
				'Jean',
				'Jean-baptiste',
				'Jean-marie',
				'Jeannot',
				'Jourdain',
				'Jules',
				'Julien',
				'Juste',
				'Laurent',
				'Lazare',
				'Lionel',
				'Loic',
				'Lothaire',
				'Louis',
				'Loup',
				'Luc',
				'Lucien',
				'Marc',
				'Marcel',
				'Marcellin',
				'Marin',
				'Mathieu',
				'Matthieu',
				'Maxime',
				'Maximilien',
				'Michel',
				'Modeste',
				'Modestine',
				'Narcisse',
				'Nazaire',
				'Nicolas',
				'Noel',
				'Olivier',
				'Onesime',
				'Papillion',
				'Pascal',
				'Paschal',
				'Patrice',
				'Perceval',
				'Philibert',
				'Philippe',
				'Pierre',
				'Pons',
				'Prosper',
				'Rainier',
				'Raoul',
				'Renard',
				'Renaud',
				'Reynaud',
				'Roch',
				'Rodolphe',
				'Rodrigue',
				'Romain',
				'Serge',
				'Sylvain',
				'Sylvestre',
				'Telesphore',
				'Theirn',
				'Thibault',
				'Thierry',
				'Toussaint',
				'Urbain',
				'Vespasien',
				'Yves',
				'Zacharie'
			]
		},
		'ma' : {
			'communs' : [
				'route de campagne le vendredi soir',
				'cabricole',
				'batterie de merde'
			],
			'noms' : [
				'Adeline',
				'Adrienne',
				'Agathe',
				'Albertine',
				'Alexandrie',
				'Aline',
				'Alphonsine',
				'Amarante',
				'Ambre',
				'Anastasie',
				'Angeline',
				'Angelique',
				'Anne',
				'Annette',
				'Antoinette',
				'Apolline',
				'Arianne',
				'Arienne',
				'Arlette',
				'Armelle',
				'Arnaude',
				'Aude',
				'Aurore',
				'Avril',
				'Axelle',
				'Benjamine',
				'Benoite',
				'Bernadette',
				'Berthe',
				'Blanche',
				'Carine',
				'Carole',
				'Caroline',
				'Cerise',
				'Chantal',
				'Charline',
				'Charlotte',
				'Christelle',
				'Christine',
				'Claire',
				'Clarisse',
				'Claudette',
				'Claudine',
				'Clementine',
				'Clothilde',
				'Colette',
				'Corinne',
				'Cosette',
				'Danielle',
				'Delphine',
				'Denise',
				'Diane',
				'Dianne',
				'Donatienne',
				'Doriane',
				'Edwige',
				'Emeline',
				'Emmanuelle',
				'Eulalie',
				'Evette',
				'Fabienne',
				'Faustine',
				'Felicienne',
				'Fernande',
				'Fifi',
				'Flavie',
				'Florette',
				'Florianne',
				'Francine',
				'Gabrielle',
				'Gaetane',
				'Georgette',
				'Georgine',
				'Germaine',
				'Gervaise',
				'Ghislaine',
				'Gigi',
				'Gilberte',
				'Giselle',
				'Gisselle',
				'Gwenaelle',
				'Henriette',
				'Honorine',
				'Hortense',
				'Hyacinthe',
				'Jacinthe',
				'Jacqueline',
				'Jeanine',
				'Jeanne',
				'Jeannette',
				'Jeannine',
				'Joceline',
				'Joelle',
				'Jolie',
				'Josette',
				'Josiane',
				'Juliane',
				'Julie',
				'Julienne',
				'Juliette',
				'Justine',
				'Laure',
				'Laurence',
				'Laurentine',
				'Laurette',
				'Liane',
				'Lisette',
				'Louise',
				'Luce',
				'Lucie',
				'Lucienne',
				'Lucile',
				'Lucille',
				'Lucinde',
				'Lucrece',
				'Lunete',
				'Lydie',
				'Madeleine',
				'Madeline',
				'Manon',
				'Marceline',
				'Marcelle',
				'Marcellette',
				'Marcelline',
				'Margot',
				'Marguerite',
				'Marianne',
				'Marie',
				'Marielle',
				'Mariette',
				'Marine',
				'Marise',
				'Marthe',
				'Martine',
				'Mathilde',
				'Maximilienne',
				'Micheline',
				'Michelle',
				'Mignon',
				'Mirabelle',
				'Mireille',
				'Monique',
				'Morgaine',
				'Morgane',
				'Myriam',
				'Nadia',
				'Nadine',
				'Natalie',
				'Nathalie',
				'Nicole',
				'Nicolette',
				'Ninette',
				'Ninon',
				'Noella',
				'Noelle',
				'Odette',
				'Odile',
				'Olivie',
				'Olympe',
				'Oriane',
				'Orianne',
				'Ouida',
				'Pascale',
				'Pascaline',
				'Paule',
				'Paulette',
				'Pauline',
				'Perrine',
				'Philippine',
				'Placide',
				'Raymonde',
				'Reine',
				'Rochelle',
				'Rolande',
				'Romaine',
				'Rosalie',
				'Roselle',
				'Rosemonde',
				'Rosette',
				'Rosine',
				'Roxane',
				'Sabine',
				'Sandrine',
				'Seraphine',
				'Sidonie',
				'Simone',
				'Solange',
				'Sophie',
				'Suzanne',
				'Suzette',
				'Sylvaine',
				'Sylviane',
				'Sylvianne',
				'Sylvie',
				'Tatienne',
				'Toinette',
				'Valentine',
				'Victoire',
				'Victorine',
				'Vienne',
				'Violette',
				'Virginie',
				'Vivienne',
				'Yolande',
				'Yseult',
				'Yvette',
				'Yvonne',
				'Zephyrine'
			]
		}
	},
	'qui' : {
		'sait' : [
			'déclarer une variable',
			'faire un serveur Free Radius'
		],
		'est' : [
			'certifié CE',
			'certifié Radius'
		]
	},
	'uniq' : {
		'obj' : {
			'mon' : [
				'datacenter spécialisé dans le stockage de masse',
				'Thrust'
			],
			'ma' : [
				'flotte de 500 000 bateaux',
				'Bugatti Chiron Super Sport 300+',
				str(random.randint(1,10000))+'e version de mon programme de '+str(random.randint(1,20000))+' lignes'
			]
		},
		'faire' : [
			'stocker mon trousseau de clé publiques',
			'faire pousser mes plantes',
			'envoyer des "il est où" à mes amis'
		]
	},
	'bah' : {
		'fait' : [
			'le naviguateur ne fait pas confiance au certificat que j\'ai signé',
			'Orange ne m\'a pas donné un routeur de bordure'
		],
		'suis' : [
			'je suis une autorité de certification',
			'je gère plusieurs AS'
		]
	},
	'profs' : {
		'prof' : [
			'Comby',
			'Druon',
			'Fafa',
			'Haddab',
			'Bobo',
			'Galy',
			'Pouget'
		],
		'quand' : [
			'il a perdu ses clés',
			'il veut prendre l\'autoroute'
		],
		'phrase' : [
			'Non mais je comprends pas c\'est pas une clé symétrique que j\'ai pourtant ?',
			'Alors d\'abord on va faire traceroute !'
		]
	},
	'www' : {
		'dn' : [
			'enboutdeligne',
			'jsuispassitanttoncodequeca',
			'jaimetellementlepostfixquejensaigneraitdesdoigts',
			'impedancecaracteristique',
			'phicestcommeundephasage',
			'quandcestpluscestlapenteositive'
		],
		'ext' : [
			'decade',
			'dbm',
			'yameule',
			'jesaispas',
			'pem',
			'yeet',
			'oof'
		]
	}
}

n = 1
w = 0
i = -1
for arg in sys.argv:
	i+=1
	if arg == "-m":
		message = str(sys.argv[i+1])
	if arg == "-d":
		names = str(sys.argv[i+1])
		names = names.split(' ')
	if arg == "-p":
		p = str(sys.argv[i+1])
	if arg == "-n":
		n = int(sys.argv[i+1])
	if arg == "-w":
		w = int(sys.argv[i+1])

if not "-d" in sys.argv:
	names = list()
	for name in friends:
		names.append(name)

def getmessage(p):
	if p == "culte":
		message = random.choice(list(phrases['culte']))
	if p == "où":
		if random.randint(0,1) == 0:
			if random.randint(0,1) == 0:
				message = "Il est où mon "+random.choice(list(phrases['où']['mon']['communs']))+" ?"
			else:
				message = "Il est où mon "+random.choice(list(phrases['où']['mon']['noms']))+" ?"
		else:
			if random.randint(0,1) == 0:
				message = "Elle est où ma "+random.choice(list(phrases['où']['ma']['communs']))+" ?"
			else:
				message = "Elle est où ma "+random.choice(list(phrases['où']['ma']['noms']))+" ?"
	if p == "qui":
		message = "Non mais c'est qui celui-là ? Il "
		if random.randint(0,1) == 0:
			message += "sait même pas "+random.choice(list(phrases['qui']['sait']))+" !"
		else:
			message += "est même pas "+random.choice(list(phrases['qui']['est']))+" !"
	if p == "uniq":
		if random.randint(0,1) == 0:
			message = "Il est où mon "+random.choice(list(phrases['uniq']['obj']['mon']))
		else:
			message = "Elle est où ma "+random.choice(list(phrases['uniq']['obj']['ma']))
		message += " me servant uniquement à "+random.choice(list(phrases['uniq']['faire']))+" ?"
	if p == "bah":
		message = "\"Bah j'comprends pas "+random.choice(list(phrases['bah']['fait']))+" pourtant "+random.choice(list(phrases['bah']['suis']))+"\""
	if p == "profs":
		message = "Ça c'est "+random.choice(list(phrases['profs']['prof']))+" quand "+random.choice(list(phrases['profs']['quand']))+" : \""+random.choice(list(phrases['profs']['phrase']))+"\""
	if p == "www":
		message = "www."+random.choice(list(phrases['www']['dn']))+"."+random.choice(list(phrases['www']['ext']))
	return message

if "-v" in sys.argv:
	print("Message :",message)
	print("Destinataires :",names)
	print("Nombre de message par personne :",n)
	if w == 0:
		print("Temps d'attente : aucun")
	else:
		print("Temps d'attente :",w,"secondes")

for i in range(0,n):
	if not "-m" in sys.argv:
		if not "-p" in sys.argv: p = random.choice(list(phrases.keys()))
		message = getmessage(p)
	for name in names:
		if name in friends:
			print("\""+message+"\"","->",friends[name]['CN'],"(ID : "+str(friends[name]['ID'])+")")
			if not "-t" in sys.argv: client.send(Message(text=message),thread_id=friends[name]['ID'])
		else:
			print("\""+name+"\"","n'est pas dans la BDD.")
	if i < n-1 and w > 0: time.sleep(w)

if not "-t" in sys.argv: client.logout()