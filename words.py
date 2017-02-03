# creating a dictionary function
def meaning(word):
    
    # words definition
    sevenDef = "equivalent to the sum of three and four"
    worldDef = "the earth, together with all of its countries and peoples"
    aboutDef = "used to indicate movement within a particular area"
    againDef = "another time; once more"
    heartDef = "a hollow muscular organ that pumps the blood through the circulatory system"
    pizzaDef = "a dish of Italian origin, consisting of a flat round base of dough baked with a topping of tomatoes and cheese"
    waterDef = "a colourless, transparent, odourless, liquid"
    happyDef = "feeling or showing pleasure or contentment"
    sixtyDef = "the number equivalent to the product of six and ten"
    boardDef = "a long, thin, flat piece of wood or other hard material"
    monthDef = "each of the twelve named periods into which a year is divided"
    angelDef = "a spiritual being believed to act as an attendant, agent, or messenger of God"
    deathDef = "the action or fact of being killed"
    greenDef = "of the colour between blue and yellow in the spectrum"
    musicDef = "vocal or instrumental sounds combined to produce harmony"
    fiftyDef = "the number equivalent to the product of five and ten"
    threeDef = "equivalent to the sum of one and two"
    partyDef = "a social gathering of invited guests"
    pianoDef = "a large keyboard musical instrument with a wooden case"
    tigerDef = "a very large solitary cat with a yellow-brown coat striped with black"
    faithDef = "complete trust or confidence in someone or something"
    earthDef = "the planet on which we live"
    riverDef = "a large natural stream of water flowing in a channel to the sea"
    moneyDef = "a current medium of exchange"
    peaceDef = "freedom from disturbance"
    fortyDef = "the number equivalent to the product of four and ten"
    smileDef = "a pleased, kind, or amused facial expression"
    abateDef = "make (something) less intense"
    houseDef = "a building for human habitation"
    aloneDef = "having no one else present"
    watchDef = "look at or observe attentively over a period of time"
    lemonDef = "a pale yellow oval citrus fruit with thick skin and fragrant"
    southDef = "the direction towards the point of the horizon 90° clockwise from east"
    ericaDef = "a plant of the genus family Ericaceae "
    animeDef = "a style of Japanese film and television animation"
    afterDef = "in the time following an event or another period of time"
    womanDef = "an adult human female"
    santaDef = "legendary patron saint of children, commonly identified with Saint Nicholas"
    stoneDef = "hard solid non-metallic mineral matter of which rock is made"
    chinaDef = "a fine white or translucent vitrified ceramic material"
    bloodDef = "the red liquid that circulates in the arteries and veins of humans and other vertebrate animals"
    mouthDef = "the opening and cavity in the lower part of the human face"
    sugarDef = "a sweet crystalline substance obtained from various plants"
    amberDef = "hard translucent fossilized resin originating from extinct coniferous trees of the Tertiary period"
    dreamDef = "a series of thoughts, images, and sensations occurring in a person's mind during sleep."
    appleDef = "the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh."
    laughDef = "make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement and sometimes also of derision"
    error = "We ran into a problem :( please close this app and try again"
    if word == "seven":
        return sevenDef
    elif word == "world":
        return worldDef
    elif word == "about":
        return aboutDef
    elif word == "again":
        return againDef
    elif word == "pizza":
        return pizzaDef
    elif word == "heart":
        return heartDef
    elif word == "water":
        return waterDef
    elif word == "happy":
        return happyDef
    elif word == "sixty":
        return sixtyDef
    elif word == "board":
        return boardDef
    elif word == "month":
        return monthDef
    elif word == "angel":
        return angelDef
    elif word == "death":
        return deathDef
    elif word == "green":
        return greenDef
    elif word == "music":
        return musicDef
    elif word == "fifty":
        return fiftyDef
    elif word == "three":
        return threeDef
    elif word == "party":
        return partyDef
    elif word == "piano":
        return pianoDef
    elif word == "mouth":
        return mouthDef
    elif word == "woman":
        return womanDef
    elif word == "sugar":
        return sugarDef
    elif word == "amber":
        return amberDef
    elif word == "dream":
        return dreamDef
    elif word == "apple":
        return appleDef
    elif word == "laugh":
        return laughDef
    elif word == "tiger":
        return tigerDef
    elif word == "faith":
        return faithDef
    elif word == "earth":
        return earthDef
    elif word == "river":
        return riverDef
    elif word == "money":
        return moneyDef
    elif word == "peace":
        return peaceDef
    elif word == "forty":
        return fortyDef
    elif word == "smile":
        return smileDef
    elif word == "abate":
        return abateDef
    elif word == "house":
        return houseDef
    elif word == "alone":
        return aloneDef
    elif word == "watch":
        return watchDef
    elif word == "lemon":
        return lemonDef
    elif word == "south":
        return southDef
    elif word == "erica":
        return ericaDef
    elif word == "anime":
        return animeDef
    elif word == "after":
        return afterDef
    elif word == "santa":
        return santaDef
    elif word == "stone":
        return stoneDef
    elif word == "china":
        return chinaDef
    elif word == "blood":
        return bloodDef
    else:
        return error
