<template>
  <div class="container-fluid">
    <!--
    <h1>This is the Strike Em Out page</h1>
    <div class="container-fluid">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
    -->
    <!--<div class="display-4">Strike 'em Out</div>-->
    <b-row>
      <!-- Left Column-->
      <b-col>
        <div class="display-2">Strike 'em Out</div>
        <!-- Select Pitcher -->
        <b-row align-v="center" align-h="center" class="mt-5 mb-3">
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
        <!-- Advanced Settings -->
        <b-card title="Advanced Settings" bg-variant="light" class="ml-5 mr-5 mb-5">
          <b-form-group>
            <b-form-checkbox-group v-model="baseRunners" :options="onBase" buttons class="mb-3"/>
            <b-form-radio-group v-model="alpha" :options="alphas" buttons class="mb-3"/>
            <b-form-radio-group v-model="sampleSize" :options="sampleSizes" buttons/>
          </b-form-group>
        </b-card>
        <!-- Power Sequences -->
        <b-card title="Power Sequences" bg-variant="light" class="ml-5 mr-5">
          <b-table :items="sequences"/>
        </b-card>
      </b-col>
      <!-- Right Column-->
      <b-col class="mr-5">
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
                             v-bind:key="player" v-bind:value="player">
              {{ player }}
            </b-select-option>
          </b-select>
        </b-row>
        <!--
        <p v-if="selectedTeam&&selectedPlayer">
          You selected a {{ selectedTeam.label }} and specifically {{ selectedPlayer }}.
        </p>
        -->
        <img src="../assets/Batter_at_bat.png" alt="Batter at bat"
             style="height: 815px; width: 550px;"/>
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
        { text: 'First Base', value: '1' },
        { text: 'Second Base', value: '2' },
        { text: 'Third Base', value: '3' },
      ],

      alpha: '2',
      alphas: [
        { text: 'alpha value 1', value: '1' },
        { text: 'alpha value 2', value: '2' },
        { text: 'alpha value 3', value: '3' },
      ],

      sampleSize: '1',
      sampleSizes: [
        { text: 'sample size 1', value: '1' },
        { text: 'sample size 2', value: '2' },
        { text: 'sample size 3', value: '3' },
      ],

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
