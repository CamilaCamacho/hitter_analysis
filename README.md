# Hitter Flashcards for Pitchers

Analyzing the success/failure rate per pitch type per location for MLB hitters. 
Ideally, we would like to be able to analyze and display all MLB hitters with an understanding of who the pitcher is and use clusterings of pitchers to show how the batter will respond to specific pitchers.

## Original Data Set
[This CSV file](https://github.com/CamilaCamacho/hitter_analysis/blob/master/savant_data_6_pitchers.csv) has all 2019 Regular Season [Savant data from Statcast Search](https://baseballsavant.mlb.com/statcast_search?hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea=2019%7C&hfSit=&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfInfield=&team=&position=&hfOutfield=&hfRO=&home_road=&batters_lookup%5B%5D=660670&batters_lookup%5B%5D=641313&batters_lookup%5B%5D=641355&batters_lookup%5B%5D=593160&batters_lookup%5B%5D=545361&batters_lookup%5B%5D=592885&hfFlag=&hfPull=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_pas=0#results) for the following 6 hitters/batters: 
1. Ronald Acuna Jr. (660670)
2. Tim Anderson (641313)
3. Cody Bellinger (641355)
4. Whit Merrifield (593160)
5. Mike Trout (545361)
6. Christian Yelich (592885)

[Statcast Search Documentation](https://baseballsavant.mlb.com/csv-docs#events) gives brief descriptions of CSV data. Analysis will be done using [this Excel doc](https://github.com/CamilaCamacho/hitter_analysis/blob/master/savant_data_analysis_6_pitchers.xlsx) where redundant/deprecated data has been deleted and useful data has been reorganized. Below you'll find a more in-depth description of relevant data-points found in this data set.

### Pitch Types
* CH: Change-up
* CU: Curveball
* FC: Cutter
* FF: Four-Seam Fastball
* FS: Splitter
* FT: Two-Seam Fastball (synonymous with SI)
* KC: Knuckle Curve
* KN: Knuckleball
* SI: Sinker (synonymous with FT)
* SL: Slider 
* null

Pitch Types not present in this dataset: AB, AS, EP, FO, GY, IN, NP, PO, SC, UN

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

### Type: Pitch Result 
* B: ball
* S: strike
* X: in play
  * A ball is “in play” when the plate appearance ends in something other than a strikeout, walk, hit batter, catcher’s interference, sacrifice bunt, or home run. 

### Batted Ball Type
* fly_ball
* ground_ball
* line_drive
* null
* popup

### Zones: Location of ball as it crosses plate (catcher's perspective)
![Gameday Zones](https://github.com/CamilaCamacho/hitter_analysis/blob/master/screenshots/gameday-zones.png)

## Initial Clustering
We will begin by clustering the success/failure rate for each pitch type for each location.
Success/failure will be determined by 
