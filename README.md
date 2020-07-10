# Strike 'em Out: A Visual Analysis MLB Hitter Weaknesses

Analyzing the success rate of different pitch types for a given pitcher cluster within the determined strike zone for MLB hitters. 

The website www.strike-em-out.jhu.edu analyzes and displays the success/failure rate for different pitch types in the strikezone of Major League Baseball (MLB) batters depending on who the pitcher is as well as the circumstances of the game. The analysis takes into account the velocity and movement of pitches to cluster similar pitch types of different pitchers together. 

## 2019 Regular Season Data Set Documentation

[Edited 2019 Regular Season Data Set JSON file](https://github.com/CamilaCamacho/hitter_analysis/blob/master/CleanedUpForDB-final.json) is taken from [2019 Regular Season Data Set CSV file]() but paired down to the more relevant data points. 


[Statcast Search Documentation](https://baseballsavant.mlb.com/csv-docs#events) gives brief descriptions of the CSV data. 


[2019 MLB Regular Season data set]() from Statcast was edited down to relevant data points to [2019 Regular Season (CleanedUpForDB) CSV](). Then, [other calculations were done](https://github.com/CamilaCamacho/hitter_analysis/blob/master/DB_Filtering_Computations.ipynb) to find which zone and pitch type clustering each pitch falls into to create [a database of all pitches ](https://github.com/CamilaCamacho/hitter_analysis/blob/master/all_2019_pitches.json).

### Pitch ID
Since the pitch_id field is deprecated, we will be creating our own unique pitch id using:
* game_pk: Unique Id for Game
* sv_id: Non-unique Id of play event per game (a date/time stamp of when the PITCHf/x tracking system first detected the pitch in the air, it is in the format YYMMDD_hhmmss).
 * _Note: The YYMMDD date does not always match game_date M/D/YYYY for some reason (probably because of timezones)_


### Pitch Types
**The type of pitch derived from Statcast**
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

### Description: 
**Description of the resulting pitch**
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

### Events: 
**Baserunning Event that occurs during the Plate Appearance**
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

#### Plate_-X & Plate_Z:
**Horizontal & Vertical position of the ball when it crosses home plate from the pitcher's perspective**
_Note: Plate\_-x is different from statcast's plate\_x, it's the negated version so that is from pitcher's perspective_

The center of home plate is at ground level and corresponds to point (0,0).

Plate -X = distance of ball in feet to the right (positive) or left (negative) of center of plate 
Plate Z = hight of ball in feet above the ground


Since the vertical limits of the strikezone depend on the height and and stance of the batter, MLBAM also provides parameters sz_top and sz_bot, which estimate the top and bottom of the strike zone for each batter.

### Zones: 
**Location of the ball when it crosses the plate from the pitcher's perspective**
_Note: Our strikezone is different from [statcast's gameday zone](https://github.com/CamilaCamacho/hitter_analysis/blob/master/screenshots/gameday-zones.png) that is from catcher's perspective_

![Our Strike Zone](https://github.com/CamilaCamacho/hitter_analysis/blob/master/screenshots/StrikeZone21Sections.png)

Length of strike zone is 17 inches, aka the length of home plate.
Height of strike zone is the distance between batter's knees (sz_bot in Statcast data) and the midpoint of their torso (sz_top in Statcast data). 

On average, this between 1.5 and 3.5 feet off the ground but we've calculated the strikezone based on the sz_bot & sz_top of each player at bat.


### Initial Clustering
...
