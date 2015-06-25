Game Ideas posted by Adam. Please edit / comment.

##Working Title: Mario A/B Decision Game

###Collection Used:		
BL Flickr Images

###Collection Size:		
1 million images, 50gb? (530GB actually)

###Interaction
A simple side scroller game (like the Phaser.io tutorial), with a little dude who runs around / swims / flies through short levels, avoiding obstacles like the Mario Koopas (but maybe with heads taken from the image collection?), spikes, pits, etc. At each screen there's a decision to make (eg, one of two doors to go through / pipes to go down). The player must decide which option is 'correct' based on an image from the Flickr colleciton. They're told to take door A, for example, if the image contains a human face, or door B if it does not. 

    Could use an on-rails type of gameplay? eg look at bittrip runner for example?

###Validation	
For most of the images, we don't actually know if A or B is the correct answer. But there are a few control images that we do know the answer (including the LAST decision). To beat the game / level, the player has to get all of the control decisions correct and avoid the obstacles. Data is collected on the non-control decisions and validated by cross-player agreement over time.


###Why this is useful	
It helps classify images at a high level.

###Why this is fun	
This is effectively Mario. The enemies to avoid make the levels challenging, and the players will be under the impression that all of their door decisions matter, making them feel like they are making choices that affect their progress in the game. Only some of them will matter, but they won't know that because if they get the last one wrong they can't win.

---

##Working Title: Tetris Game

###Collection Used:		
BL Flickr Images

###Collection Size:		
1 million images, 50gb?

###Interaction
 Images fall from the top of the screen, randomly from along the y axis. They fall at a stable rate until they hit the bottom or another block. The images are blacked out while falling - coloured shapes the size of the original image (or scaled, but the same shape). The game is over when the blocks hit the top of the screen. The rate of fall increases over time, making the game more difficult. This is effectively like tetris, but without the rotation options, and the player does not control the falling images.
 
 Instead, the player controls a little dude at the bottom of the screen. The dude runs along the bottom y axis, and when he gets to a block, the image behind it appears in a zoom window on the right of the screen, so the player can see the image at a decent size. Their job is to classify it based on one of three criteria (person, place, thing, neither, etc). Once classified, the block disappears and the remaining blocks resettle based on gravity. The player then has to run to the next blocks and do the same.
 
 There could also be additional items that fall from the top of the scree. Eg, stars to clear the whole screen, bombs that damage the 'health' of the player if he is too near when it lands. Hearts to repair health. 1-ups for extra lives, etc.
 
###Validation	

Images appear more than once during the game. If you classify them differently, you die / lose health. That prevents people from constantly hitting the same classification button over and over. There will also be 50 known images for each category, so if the person gets those wrong, again they die / lose health. Once an image has been classified on the machine 10 times in the same way, it joins the 'control' group. Images that prove contentious and have different classifications by different users, will not be used for control and will be removed from the game unless a clear preference over time develops.


###Why this is useful	
It helps classify images at a high level.

###Why this is fun	
It draws on the fun of tetris, and as it continues to speed up, is challenging. It also requires the user to make choices about the content quickly, as well as choices about the little man (which block to tackle next). Their decisions affect their progress in the game. Unlike most crowdsourcing activities, you can lose / die in this game, which I believe actually makes it a game.

---

##Working Title: 		Tinder Image Classifier

###Collection Used:		
BL Flickr Images

###Collection Size:		
1 million images, 50gb?

###Interaction	
  Joystick left or right to quickly classify images based on a question / criteria defined by us (see metadata collected). The question could be fixed, or could be randomized. This mimics the ‘Tinder’ app for online matchmaking. Left = yes, Right = no. Could have 4 motions (up, down, left, right) because of the nature of the joystick. Very short interaction with each image. Could be as fast as 1 per second. Potential for high through-put. Perhaps a countdown timer to keep them moving quickly.

	Images should be shown to scale.

	Users could gain points for each image classified, which could be used to unlock other levels / mini-games / rewards. Ideally, the metadata collected is intelligently incorporated in to the game for future players. So the subsets created with ‘face / no face’, once they reach a critical mass, trigger a new game: ‘glasses / no glasses’ or ‘beard / no beard’. Maybe these new games are ‘unlocked’ and users are challenged to help us reach goals that then allow those future classifications. Almost like we’re all playing together.

	Button 1 could be used to request that the image on the screen be emailed to you (then you submit your email address).

	Button 2 could let the user stop on a particular image and fill in the full set of metadata.


###Metadata Collected:

Possible a/b/c/d questions
•	Primarily animal/vegetable/mineral/other
•	In focus / bit blurry
•	I know what this is / no idea what this is
•	Face / no face
o	Glasses /no glasses
o	Beard / no beard
o	Male / female
o	Old / young /adult
o	Etc etc…


###Validation	

Validated by seeking classification agreement across multiple users. As far as I know, none of these details are known in the metadata.


###Why this is useful	
It’s a very quick game and easy enough to build, I think. The iterative improvements to the metadata could result in quite a few new classifications in the Flickr collection.

###Why this is fun	
Fairly mindless. Quickness of the interaction is the real appeal. The unlocking new levels may be appealing.

---


##Working Title: 		Image Gradients

###Collection Used:		
BL Flickr Images

###Collection Size:		
1 million images, 50gb?


###Interaction	
  Users are given an endless stream of images, and asked to classify them by their level of photo-realism. They align the image with its corresponding equivalent shown at the bottom of the screen. This is done via the joystick and then a button-press.

	As above, these classifications could be reincorporated into the game for building future subsets that are used in other parts of the game. A game that learns effectively.

	Since art styles change dramatically over time, it would be worth limiting the images shown to a particular user in a particular session by the date of publication of the book from which the image came. That won’t work perfectly, but it should make it a bit more similar.


###Metadata Collected:	
For each image, we get a sense of the level of detail in the image itself. How closely it resembles a photograph.
 

###Validation	
Validated by seeking classification agreement across multiple users. As far as I know, none of these details are known in the metadata.


###Why this is useful	
This has advantages because it makes it possible to show users comparable images in other games, instead of putting a scribble next to a photo.

###Why this is fun	
Good question. Would probably have to limit this to a few interactions and then get someone to move on to something else. Maybe do 5 and then be taken to a more fun game.


---

###Working Title		
Image Age Trivia

###Collection Used:	
BL Flickr Images

###Collection Size:		
1 million images, 50gb?

###Interaction	
Users are shown 3 images randomly drawn from the collection (perhaps those classified above by level of photorealism) and are asked to guess which one is the oldest / newest.

    This is great. Simple to implement, a nice challenge and should result in some interesting data to analyse about the level of illustration quality and to see if it coorelates with any metadata we have on them (publisher, cost maybe, etc)

###Metadata Collected:	
Data on how well the users are able to judge the relative age of an image.

###Validation	
Validated with metadata about the publication date of the book. This will fail in some instances where the image is a reproduction of a much earlier work.


###Why this is useful	
People like to test themselves, so this could be a breather game in between more serious collection.

###Why this is fun	
People like to test themselves. This will appeal to some people more than others. Someone with no idea of any of the answers will find this unrewarding.

---



###Working Title		Crime Robot

###Collection Used:		
Old Bailey Online criminal trial transcripts

###Collection Size:		
127 million words of text

###Interaction	
Users are shown 1 paragraph of text, and using a little avatar they are asked to move their dude over specific types of information in the paragraph and effectively tag it by clicking on the button.


###Metadata Collected:	
Range of possibilities:
-	time of crime (could be a clock-like interface)
-	items stolen
-	value of items stolen.
				


###Validation	
It’s possible to extract a lot of this stuff semi-automatically, but the human would be validating that semi-automatic work, and might also find additional details missed by the other process.

    Might be that the joystick lets people switch between text that is highlighted as a useful noun-phrase.


###Why this is useful	
Fits with my research needs to structure this data, and also tests a way to work with textual crowdsourcing that doesn’t involve a keyboard.

###Why this is fun	
Not sure it is. Non-keyboard text-based crowdsourcing.

----

###Working Title:
Slot machine Matchup

###Collection Used:
Images with contextual information about what they contain (eg tagged imgs from Flickr)

###Collection Size:
~160,000 (although a large chunk, ~54k of this is maps)

###Interaction:
Presented like a three reel slot machine, with three hold buttons underneath them. The left and center reels have already been held, each showing an image of a type (eg map). A variety of images 'spin' in the rightmost wheel, and the user has to hit the 'hold' button to stop the wheel on the matching image.

As they progress, the wheel spins faster and faster. The driver would be to make a big deal of the high score, and we can block the usual three letter suspects and let them enter their initials.

###Metadata Collected:	
Confirmation that images from a given set match, at least visually. Potential to gain more metadata by presenting a list of images, with one definite correct answer (we'll need to make a golden set of each type we use) with the maybe's (images tagged by users, but not in the golden set.)

 Can you expand on how we get new data? Wouldn't we have to know the answers for this to work?

###Validation:
They progress if they hit a match, fail if they don't. Each player can have 3 respins, and are given the choice when they have held an image, in case they didn't hold the right one. Only told if it is correct if they don't or cannot respin.

###Why this is useful:
Tag validation.

###Why this is fun:
Slot machine presentation lets us use colours and motion to feedback. With a headset, we can work in fun audio illusions (eg Shepard’s ascending tones) to help ramp up the tension. Increasing speed each level is also useful.

----

(Template:)
###Working Title:

###Collection Used:

###Collection Size:

###Interaction:

###Metadata Collected:	

###Validation:

###Why this is useful:

###Why this is fun:
