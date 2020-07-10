# Strike 'em Out: A Visual Analysis MLB Hitter Weaknesses

Analyzing the success rate of different pitch types for a given pitcher cluster within the determined strike zone for MLB hitters. 

The website www.strike-em-out.jhu.edu analyzes and displays the success/failure rate for different pitch types in the strikezone of Major League Baseball (MLB) batters. The analysis takes into account the velocity and movement of pitches, as well as the circumstances of the game. Pitchers can be clustered to similar pitchers to see how a 

Ideally, we would like to be able to analyze and display all MLB hitters with an understanding of who the pitcher is and use clusterings of pitchers to show how the batter will respond to specific pitchers.


analysis and display all Major League Baseball (MLB)
hitters with an understanding of who the pitcher is, the
velocity of the pitch, and some situational markers
from the inning. It will use clustering of pitchers to
show how the batter will respond to these specific
pitchers.

## 2019 Regular Season Data Set Documentation
... 

[Statcast Search Documentation](https://baseballsavant.mlb.com/csv-docs#events) gives brief descriptions of the CSV data. Analysis will be done using [this Excel doc](https://github.com/CamilaCamacho/hitter_analysis/blob/master/savant_data_analysis_6_pitchers.xlsx) where redundant/deprecated data has been deleted and useful data has been reorganized. Below you'll find a more in-depth description of relevant data-points found in this data set.

### Pitch ID
Since the pitch_id field is deprecated, we will be creating our own unique pitch id using:
* game_pk: Unique Id for Game
* sv_id: Non-unique Id of play event per game (a date/time stamp of when the PITCHf/x tracking system first detected the pitch in the air, it is in the format YYMMDD_hhmmss).
 * _Note: The YYMMDD date does not always match game_date M/D/YYYY for some reason (probably because of timezones)_


### Pitch Types
* CH: Change-up
* CU: Curveball
* EP: Eephus
* FC: Cutter
* FF: Four-Seam Fastball
* FO: Forkball
* FS: Splitter
* FT: Two-Seam Fastball (synonymous with SI)
* KC: Knuckle Curve
* KN: Knuckleball
* SI: Sinker (synonymous with FT)
* SL: Slider 

Pitch Types not present in this dataset: AB, AS, GY, IN, NP, PO, SC, UN

### Description of Resulting Pitch 
* ball
* blocked_ball
* called_strike
* foul
* foul_bunt
* foul_tip
* hit_by_pitch
* hit_into_play
* hit_into_play_no_out
* hit_into_play_score
* missed_bunt
* pitchout
* swinging_strike
* swinging_strike_blocked

### Events: Result of Plate Appearance
Baserunning event that occurs during the plate appearance. 
* catcher_interf
* caught_stealing_2b
* double
* double_play
* field_error
* field_out
* fielders_choice 
* fielders_choice_out
* force_out
* grounded_into_double_play
* hit_by_pitch
* home_run
* null
* other_out
* pickoff_caught_stealing_2b
* sac_fly
* single
* strikeout
* strikeout_double_play
* triple
* walk

### Zones: Location of ball as it crosses plate 

![Strike Zone Coordinates]()

Length of strike zone is 17 inches- length of home plate.
Height of strike zone is distance between batter's knees and the midpoint of their torso. Top of strike zone is the midpoint betweek the top of the batter's shoulders and the top of the uniform pants. 
the bottom of the stirke zone is at the hollow beneath the kneecap, both determined by the bater's stance as the batter prepares to swing. 
On average, between 1.5 and 3.5 feet off the ground.


![Gameday Zones from catcher's perspective](https://github.com/CamilaCamacho/hitter_analysis/blob/master/screenshots/gameday-zones.png)

![Our Strike Zone](https://github.com/CamilaCamacho/hitter_analysis/blob/master/screenshots/StrikeZone21Sections.png)


#### Plate X & Plate Z
Plate X and Plate Z are horiz and vert pitch location 
indicating the horizontal and vertical position (in feet) of the ball as it crosses the front of home plate, where the center of the plate at ground level corresponds to the point (0, 0). Since the vertical limits of the strike zone depend on the height and and stance of the batter, MLBAM also provides parameters sz_top and sz_bot, which estimate the top and bottom of the strike zone for each batter.

(Plate X = feet to R or L of center of the plate, Plate Z = height above ground). 
I *think* Normalized Plate X/Z prob adjusts for different strike zones of different batters, but not 100% sure (I never use the normalized ones)

## Initial Clustering
We will begin by clustering the success/failure rate for each pitch type for each location.
Success/failure will be determined by 
