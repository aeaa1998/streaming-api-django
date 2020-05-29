import os, django , random
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE","finalProjectApi.settings")
django.setup()


from faker import Faker
from albums.models import Album
from profiles.models import Profile 
from artists.models import Artist 
from tracks.models import Genre, Track

genresList = ['Rock','Hip Hop','Jazz','Pop Music','Folk Music','Blues','Country Music',
'Musical Theatre',' Heavy Metal','Rhythm and Blues','Punk Rock','Classical Music',
'Soul Music','Reggae','House Music','Singing',
'Funk','Disco','Techno','Electronic Dance Music','Electronic Music','Ambient Music',
'Instrumental','Alternative Rock','Trance Music','Gospel Music',
'Dance Music','Popular Music','Swing Music','Drum and Bass','Electro','Psychedelic Music',
'Dubstep','Industrial Music','Orchestra','Hardcore','Opera','Progressive Rock','Breakbeat','Dub',
'Experimental Music','Synth-pop',
'Ska','World','Indie Rock','Baroque Music','Grunge','Pop Rock','Music of Africa','Reggaeton','Bachatai','Cumbia',
]


#generrates random artists
def create_artist (amountOfArtists):
	fake = Faker ()
	for x in range (amountOfArtists):
		id=14
		myName= fake.name()
		myBio= fake.text()
		currentTime = datetime.now()
		Artist.objects.create(name= myName, bio= myBio)
		print( "-New artist created (X"+ str(x) +")")



amountOfArtists = int(input("How many artist do you want to generate? "))
create_artist(amountOfArtists)

def createGenres () :
	for x in genresList :
		myName= x
		print(x)
		Genre.objects.create(name=myName)
		print( "-New genre created")

#generrates random genres

if (len( Genre.objects.all())== 0 ):
	createGenres()
	print("just Created all the Genres")
else:
	print("It seems like Genres already exist")



# ##generates random albums

def create_albums (amountOfAlbums):
	fake= Faker()
	existingArtists= len(Artist.objects.all())
	for x in range (amountOfAlbums):
		#try:
			myTitle = fake.text(25)
			myPrice= random.uniform(0.99,15.99)
			myArtist= random.randint(1,existingArtists)
			Album.objects.create(
				title=myTitle,
				price=myPrice,
				artist=Artist.objects.get(id=myArtist)
				)
			print( "-New album created (X"+ str(x) +")")
			## se crea con canciones adentro
			existingGenres= len(Genre.objects.all())
			amountOfTracks= random.randint(7,20)
			myAlbumId= len(Album.objects.all())
			myGenre= random.randint(1,existingGenres)
			for x in range (amountOfTracks):
				try:
					myName = fake.text(25)				
					myPrice2= myPrice / amountOfTracks
					mySeconds = random.randint(120,500)
					#myExplicitLyrics= random.choice [0,1]

					Track.objects.create(
						name=myName,
						price=myPrice2,
						seconds=mySeconds,
						album=Album.objects.get(id=myAlbumId),
						genre=Genre.objects.get(id=myGenre),
						)
					print("        -New track created (X"+ str(x) +")")
				except Exception as e:
					print(e)
					print("**Could not generate a Track (" + str(x)+")")





		# except:
		# 	print("**Colud not generate an album (" + str(x)+")")
			

amountOfAlbums = int(input("How many Albums do you want to generate? "))
create_albums(amountOfAlbums)
