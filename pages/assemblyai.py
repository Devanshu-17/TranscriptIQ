import assemblyai as aai
aai.settings.api_key = f"b8e384fd6d7d48c78403c63cf532f1b4"

config = aai.TranscriptionConfig(entity_detection=True)
FILE_URL = "https://www.youtube.com/watch?v=a4Bojjx_Dew&pp=ygUiZ2V0dHlzYnVyZyBhZGRyZXNzIHNwZWVjaCBkZWxpdmVyeQ%3D%3D"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

print(transcript.text) # i.e. "Dan Gilbert"
print(transcript.entities) # i.e. EntityType.person

for entity in transcript.entities:
  print(entity.text) # i.e. "Dan Gilbert"
  print(entity.entity_type) # i.e. EntityType.person
  print(f"Timestamp: {entity.start} - {entity.end}")


# Output:
# Smoke from hundreds of wildfires in Canada is triggering air quality alerts throughout the US. Skylines from Maine to Maryland to Minnesota are gray and smoggy. And in some places, the air quality warnings include the warning to stay inside. We wanted to better understand what's happening here and why, so we called Peter DiCarlo, an associate professor in the Department of Environmental Health and Engineering at Johns Hopkins University. Good morning, professor. Good morning. So what is it about the conditions right now that have caused this round of wildfires to affect so many people so far away? Well, there's a couple of things. The season has been pretty dry already, and then the fact that we're getting hit in the US. Is because there's a couple of weather systems that are essentially channeling the smoke from those Canadian wildfires through Pennsylvania into the Mid Atlantic and the Northeast and kind of just dropping the smoke there. So what is it in this haze that makes it harmful? And I'm assuming it is is it is the levels outside right now in Baltimore are considered unhealthy. And most of that is due to what's called particulate matter, which are tiny particles, microscopic smaller than the width of your hair, that can get into your lungs and impact your respiratory system, your cardiovascular system, and even your neurological your brain. What makes this particularly harmful? Is it the volume of particulate? Is it something in particular? What is it exactly? Can you just drill down on that a little bit more? Yeah. So the concentration of particulate matter I was looking at some of the monitors that we have was reaching levels of what are, in science speak, 150 micrograms per meter cubed, which is more than ten times what the annual average should be, and about four times higher than what you're supposed to have on a 24 hours average. And so the concentrations of these particles in the air are just much, much higher than we typically see. And exposure to those high levels can lead to a host of health problems. And who is most vulnerable? I noticed that in New York City, for example, they're canceling outdoor activities, and so here it is in the early days of summer, and they have to keep all the kids inside. So who tends to be vulnerable in a situation like this? It's the youngest. So children, obviously, whose bodies are still developing. The elderly who know their bodies are more in decline, and they're more susceptible to the health impacts of breathing, the poor air quality. And then people who have preexisting health conditions, people with respiratory conditions or heart conditions can be triggered by high levels of air pollution. Could this get worse? That's a good in some areas, it's much worse than others. And it just depends on kind of where the smoke is concentrated. I think New York has some of the higher concentrations right now, but that's going to change as that air moves away from the New York area. But over the course of the next few days, we will see different areas being hit at different times with the highest concentrations. I was going to ask you, more fires start burning, I don't expect the concentrations to go up too much higher. I was going to ask you and you started to answer this, but how much longer could this last? Or forgive me if I'm asking you to speculate, but what do you think? Well, I think the fires are going to burn for a little bit longer, but the key for us in the US. Is the weather system changing. And so right now, it's kind of the weather systems that are pulling that air into our mid Atlantic and Northeast region. As those weather systems change and shift, we'll see that smoke going elsewhere and not impact us in this region as much. And so I think that's going to be the defining factor. And I think the next couple of days we're going to see a shift in that weather pattern and start to push the smoke away from where we are. And finally, with the impacts of climate change, we are seeing more wildfires. Will we be seeing more of these kinds of wide ranging air quality consequences or circumstances? I mean, that is one of the predictions for climate change. Looking into the future, the fire season is starting earlier and lasting longer and we're seeing more frequent fires. So, yeah, this is probably something that we'll be seeing more frequently. This tends to be much more of an issue in the Western US. So the Eastern US getting hit right now is a little bit new. But yeah, I think with climate change moving forward, this is something that is going to happen more frequently. That's Peter DiCarlo, associate professor in the Department of Environmental Health and Engineering at Johns Hopkins University. Sergeant Carlo, thanks so much for joining us and sharing this expertise with us. Thank you for having me.
# [Entity(entity_type=<EntityType.location: 'location'>, text='Canada', start=2548, end=3130), Entity(entity_type=<EntityType.location: 'location'>, text='the US', start=5498, end=6350), Entity(entity_type=<EntityType.location: 'location'>, text='Maine', start=7572, end=7962), Entity(entity_type=<EntityType.location: 'location'>, text='Maryland', start=8228, end=8650), Entity(entity_type=<EntityType.location: 'location'>, text='Minnesota', start=8948, end=9610), Entity(entity_type=<EntityType.person_name: 'person_name'>, text='Peter DiCarlo', start=18948, end=20010), Entity(entity_type=<EntityType.occupation: 'occupation'>, text='associate professor', start=20308, end=21226), Entity(entity_type=<EntityType.organization: 'organization'>, text='Department of Environmental Health and Engineering', start=21508, end=23706), Entity(entity_type=<EntityType.organization: 'organization'>, text='Johns Hopkins University', start=23972, end=25426), Entity(entity_type=<EntityType.occupation: 'occupation'>, text='professor', start=26076, end=26950), Entity(entity_type=<EntityType.location: 'location'>, text='the US', start=45184, end=45946), Entity(entity_type=<EntityType.nationality: 'nationality'>, text='Canadian', start=49728, end=50086), Entity(entity_type=<EntityType.location: 'location'>, text='Pennsylvania', start=51696, end=52326), Entity(entity_type=<EntityType.location: 'location'>, text='Mid Atlantic', start=52624, end=53178), Entity(entity_type=<EntityType.location: 'location'>, text='Northeast', start=53364, end=53914), Entity(entity_type=<EntityType.location: 'location'>, text='Baltimore', start=65064, end=65534), Entity(entity_type=<EntityType.occupation: 'occupation'>, text='science', start=101168, end=101414), Entity(entity_type=<EntityType.location: 'location'>, text='New York City', start=125768, end=126274), Entity(entity_type=<EntityType.medical_condition: 'medical_condition'>, text='respiratory conditions', start=153028, end=153786), Entity(entity_type=<EntityType.medical_condition: 'medical_condition'>, text='heart conditions', start=153988, end=154506), Entity(entity_type=<EntityType.location: 'location'>, text='New York', start=171448, end=171970), Entity(entity_type=<EntityType.location: 'location'>, text='New York', start=175944, end=176322), Entity(entity_type=<EntityType.location: 'location'>, text='the US', start=201824, end=202250), Entity(entity_type=<EntityType.location: 'location'>, text='mid Atlantic', start=209090, end=209866), Entity(entity_type=<EntityType.location: 'location'>, text='Northeast region', start=210196, end=211130), Entity(entity_type=<EntityType.location: 'location'>, text='Western US', start=257364, end=258046), Entity(entity_type=<EntityType.location: 'location'>, text='Eastern US', start=258484, end=259054), Entity(entity_type=<EntityType.person_name: 'person_name'>, text='Peter DiCarlo', start=268298, end=269194), Entity(entity_type=<EntityType.occupation: 'occupation'>, text='associate professor', start=269242, end=270186), Entity(entity_type=<EntityType.organization: 'organization'>, text='Department of Environmental Health and Engineering', start=270468, end=272810), Entity(entity_type=<EntityType.organization: 'organization'>, text='Johns Hopkins University', start=273172, end=274882), Entity(entity_type=<EntityType.occupation: 'occupation'>, text='Sergeant', start=274986, end=275298), Entity(entity_type=<EntityType.person_name: 'person_name'>, text='Carlo', start=275314, end=275634)]
# Canada
# EntityType.location
# Timestamp: 2548 - 3130
# the US
# EntityType.location
# Timestamp: 5498 - 6350
# Maine
# EntityType.location
# Timestamp: 7572 - 7962
# Maryland
# EntityType.location
# Timestamp: 8228 - 8650
# Minnesota
# EntityType.location
# Timestamp: 8948 - 9610
# Peter DiCarlo
# EntityType.person_name
# Timestamp: 18948 - 20010
# associate professor
# EntityType.occupation
# Timestamp: 20308 - 21226
# Department of Environmental Health and Engineering
# EntityType.organization
# Timestamp: 21508 - 23706
# Johns Hopkins University
# EntityType.organization
# Timestamp: 23972 - 25426
# professor
# EntityType.occupation
# Timestamp: 26076 - 26950
# the US
# EntityType.location
# Timestamp: 45184 - 45946
# Canadian
# EntityType.nationality
# Timestamp: 49728 - 50086
# Pennsylvania
# EntityType.location
# Timestamp: 51696 - 52326
# Mid Atlantic
# EntityType.location
# Timestamp: 52624 - 53178
# Northeast
# EntityType.location
# Timestamp: 53364 - 53914
# Baltimore
# EntityType.location
# Timestamp: 65064 - 65534
# science
# EntityType.occupation
# Timestamp: 101168 - 101414
# New York City
# EntityType.location
# Timestamp: 125768 - 126274
# respiratory conditions
# EntityType.medical_condition
# Timestamp: 153028 - 153786
# heart conditions
# EntityType.medical_condition
# Timestamp: 153988 - 154506
# New York
# EntityType.location
# Timestamp: 171448 - 171970
# New York
# EntityType.location
# Timestamp: 175944 - 176322
# the US
# EntityType.location
# Timestamp: 201824 - 202250
# mid Atlantic
# EntityType.location
# Timestamp: 209090 - 209866
# Northeast region
# EntityType.location
# Timestamp: 210196 - 211130
# Western US
# EntityType.location
# Timestamp: 257364 - 258046
# Eastern US
# EntityType.location
# Timestamp: 258484 - 259054
# Peter DiCarlo
# EntityType.person_name
# Timestamp: 268298 - 269194
# associate professor
# EntityType.occupation
# Timestamp: 269242 - 270186