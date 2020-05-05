<template>
  <div class="container-fluid">
    <!-- Top Select -->
    <b-row class="mb-3">
      <b-col>
        <div class="display-3">Strike 'em Out</div>
        <!-- Select Pitcher -->
        <b-row align-v="center" align-h="center" class="mt-3 mb-3">
          <b-select v-model="selectedPitcher" class="mr-2" style="width: 50%;">
            <b-select-option disabled value='null'>-- Select a pitcher --</b-select-option>
            <b-select-option v-for="pitcher in pitchers"
                             v-bind:value="pitcher" v-bind:key="pitcher">
              {{ pitcher }}
            </b-select-option>
          </b-select>
          <b-form-checkbox switch v-model="cluster" value="true" unchecked-value="false">
            Group like pitchers
          </b-form-checkbox>
        </b-row>
      </b-col>
      <b-col align-self="center">
        <!-- Select Team -->
        <b-row align-h="center">
          <b-select v-model="selectedTeam" class="mb-1" size="lg" style="width: 75%;">
            <b-select-option disabled value='0'>-- Select a team --</b-select-option>
            <b-select-option v-for="team in teams"
                             v-bind:value="team" v-bind:key="team">
              {{ team.label }}
            </b-select-option>
          </b-select>
        </b-row>
        <!-- Select Player from Team -->
        <b-row align-h="center">
          <b-select v-model="selectedPlayer" size="lg" style="width: 75%">
            <b-select-option disabled value=''>-- Select a player --</b-select-option>
            <b-select-option v-for="player in selectedTeam.players"
                             v-bind:value="player" v-bind:key="player">
              {{ player }}
            </b-select-option>
          </b-select>
        </b-row>
      </b-col>
    </b-row>
    <!-- Bottom Select -->
    <b-row>
      <!-- Left Column-->
      <b-col>
        <!-- Power Sequences -->
        <b-card title="Power Sequences" bg-variant="light" class="ml-5 mr-5 mb-3">
          <b-table :items="sequences"/>
        </b-card>
        <!-- Legend -->
        <b-card title="Legend" bg-variant="light" class="ml-5 mr-5 mb-3">
          <p>RED: High Likelihood of Contact</p>
          <p>YELLOW: Medium Likelihood of Contact</p>
          <p>GREEN: Low Likelihood of Contact</p>
        </b-card>
        <!-- Advanced Settings -->
        <b-button v-b-toggle.advanced-settings size="sm">Advanced Settings</b-button>
        <b-collapse id="advanced-settings" class="mt-3">
          <b-card class="ml-5 mr-5">
            <!-- Runners on Base-->
            <b-row align-h="center">
              <b-form-radio-group v-model="baseRunners" :options="onBase"
                                  buttons button-variant="light" class="mb-3"/>
            </b-row>
            <!-- Sample Size -->
            <b-row align-h="center" align-v="center" class="mb-3">
              <label for="sb-inline" class="mb-0">Sample Size</label>
              <font-awesome-icon id="sample-size-info" href="#" tabindex="0"
                                 :icon="['fas', 'info-circle']" class="ml-1 mr-3"/>
              <b-popover target="sample-size-info" placement="left" triggers="focus"
                         title="Sample Size">
                Total pitches per pitch type <br> where batter swung.
              </b-popover>
              <b-form-spinbutton id="sb-inline" min="1" max="15" v-model="sampleSize" wrap inline/>
            </b-row>
            <!-- Alpha Values
            <b-row align-h="center">
              <b-form-radio-group v-model="alpha" :options="alphas"
                                  buttons button-variant="light"/>
            </b-row> -->
          </b-card>
        </b-collapse>
      </b-col>
      <!-- Player and Strike-zone-->
      <b-col>
        <img src="../assets/Batter_at_bat.png" alt="Batter at bat"
             style="height: 915px; width: 650px;"/>
      </b-col>
    </b-row>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'StrikeEmOut',
  data() {
    return {
      msg: '',

      selectedPitcher: null,
      pitchers: [
        'Justin Verlander', 'Clayton Kershaw', 'Zack Greinke', 'Max Scherzer',
      ],

      cluster: 'false',

      baseRunners: '',
      onBase: [
        { text: 'Runners on First and/or Second Base', value: '1' },
        { text: 'No Runners on Base or Runner on Third Base', value: '2' },
      ],

      alpha: '2',
      alphas: [
        { text: 'alpha value 1', value: '1' },
        { text: 'alpha value 2', value: '2' },
        { text: 'alpha value 3', value: '3' },
      ],

      sampleSize: '5',

      sequences: [
        {
          first_pitch_type: 'FF',
          first_zone: '2',
          second_pitch_type: 'CU',
          second_zone: '1',
          frequency: '16',
        },
        {
          first_pitch_type: 'SL',
          first_zone: '3',
          second_pitch_type: 'SL',
          second_zone: '4',
          frequency: '12',
        },
        {
          first_pitch_type: 'FC',
          first_zone: '3',
          second_pitch_type: 'FF',
          second_zone: '3',
          frequency: '10',
        },
      ],

      selectedTeam: '0',
      selectedPlayer: '',
      selectedTeamLabel: '',
      players: [],
      teams: [
        {
          label: 'New York Yankees',
          players: ['Zack Britton', 'Luis Cessa', 'Aroldis Chapman', 'Gerrit Cole'],
          value: '1',
        },
        {
          label: 'Boston Red Sox',
          players: ['Matt Barnes', 'Ryan Brasier', 'Austin Brice', 'Nathan Eovaldi'],
          value: '2',
        },
        {
          label: 'Los Angeles Dodgers',
          players: ['Scott Alexander', 'Pedro Báez', 'Walker Buehler', 'Caleb Ferguson'],
          value: '3',
        },
      ],
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/strikeemout';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectTeam() {
      this.selectedPlayer = '';
      this.players = this.teams[this.selectedTeam].players;
      this.selectedTeamLabel = this.teams[this.selectedPlayer].label;
    },
  },
  created() {
    this.getMessage();
    this.selectTeam();
  },
};
</script>

<style scoped>

</style>
