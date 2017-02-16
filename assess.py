import csv
# Just fiddling with the csv package and figuring it out, 
# toying with reading and linking files and skimming data.

listings = {}
calendar = {}
reviews = {}
listingsHeaders = {}
reviewsHeaders = {}
calendarHeaders = {}

def Initialise():
	global listingsHeaders
	global reviewsHeaders
	global calendarHeaders
	global listings
	global calendar
	global reviews

	with open('listings.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if listingsHeaders == {}:
				listingsHeaders = row.keys()
			if row['id'] not in listings:
				listings[row['id']] = []
			listings[row['id']].append(row)

	with open('reviews.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if reviewsHeaders == {}:
				reviewsHeaders = row.keys()
			if row['listing_id'] not in reviews:
				reviews[row['listing_id']] = []
			reviews[row['listing_id']].append(row)

	with open('calendar.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if calendarHeaders == {}:
				calendarHeaders = row.keys()
			if row['listing_id'] not in calendar:
				calendar[row['listing_id']] = []
			calendar[row['listing_id']].append(row)

def GetColumnNames(file):
	if file == "listings":
		return listingsHeaders
		#print(', '.join(listingsHeaders))
	elif file == "calendar":
		return calendarHeaders
		#print(', '.join(calendarHeaders))
	elif file == "reviews":
		return reviewsHeaders
		#print(', '.join(reviewsHeaders))

def GetListingsByLocation(locale):
	local = []
	for listing in listings.values():
		for i in listing:
			if i['smart_location'] == locale:
				local.append(i)
	return local

def GetOpenListingsOnDate(date):
	openListings = []
	for listing in calendar.values():
		for i in listing:
			if i['date'] == date:
				openListings.append(i)
	return openListings


#def GetListingsByHost(hostName):

#def GetReviewsByReviewer(reviewerName):

#def GetListingsReviewedByReviewer(reviewerName):


Initialise()
l = GetListingsByLocation("Seattle, WA")
for item in l:
	print item['smart_location']
#GetColumnNames("listings")
#print(str(len(listings)) + ' ' + str(len(reviews)) + ' ' + str(len(calendar)))

