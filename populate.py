import os, django , random
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE","finalProjectApi.settings")
django.setup()


from faker import Faker
from albums.models import Album
from profiles.models import Profile 
from artists.models import Artist 
from tracks.models import Genre, Track


# currentTime = datetime.now()
# print(" currentTime = "+ currentTime)
# datetime.strptime(currentTime, "%Y-%m-%d %H:%M:%S.%f")


#generrates random artists
def create_artist (amountOfArtists):
	fake = Faker ()
	for x in range (amountOfArtists):
		id=14
		myName= fake.name()
		myBio= fake.text()
		currentTime = datetime.now()

		print (" Artist called : " + myName)
		print( " BIO : "+ myBio)
		#print(" currentTime = "+ currentTime)
		Artist.objects.create(name= myName, bio= myBio)

create_artist(0)

##generates random albums

def create_albums (amountOfAlbums):
	fake= Faker()
	existingArtists= len(Artist.objects.all())
	for x in range (amountOfAlbums):
		try:
			myTitle = fake.text(25)
			myPrice= random.uniform(0.99,15.99)
			myArtist= random.randint(1,existingArtists)
			print( " Album name " + myTitle)
			print("Album Price: " + str(myPrice))
			Album.objects.create(title=myTitle,price=myPrice,artist=Artist.objects.get(id=myArtist))
		except:
			print("NO se pudo agregar un album")

create_albums(0)


##generates random Tracks

def create_tracks (amountOfTracks):
	fake= Faker()
	existingArtists= len(Artist.objects.all())
	existingAlbums= len(Album.objects.all())
	existingGenres= len(Genre.objects.all())


	for x in range (amountOfTracks):
		#try:
			myName = fake.text(25)
			myAlbum= random.randint(1,existingAlbums)
			myArtist= random.randint(1,existingArtists)
			myGenre= random.randint(1,existingGenres)
			myPrice= random.uniform(0.99,15.99)
			mySeconds = random.randint(120,500)
			#myExplicitLyrics= random.choice [0,1]


			Track.objects.create(
				name=myName,
				price=myPrice,
				seconds=mySeconds,
				#explicit_lyrics=myExplicitLyrics,
				album=Album.objects.get(id=myAlbum),
				genre=Genre.objects.get(id=myGenre),
				)
			print("track agregada con exito ")
		# except:
		# 	print("NO se pudo agregar un Track")

create_tracks(10)
