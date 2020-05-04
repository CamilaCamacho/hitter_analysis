<template>
  <div class="container-fluid">
    <h1>This is the Strike Em Out page</h1>
    <!--
    <div class="container-fluid">
      <button type="button" class="btn btn-primary">{{ msg }}</button>
    </div>
    -->

    <!-- Left Column-->
    <div class="col">

    </div>

    <!-- Right Column-->
    <div class="col">
      <b-select v-model="selectedTeam">
        <option disabled value='0'>Select a team</option>
        <option v-for="team in teams" v-bind:value="team" v-bind:key="team">
          {{ team.label }}
        </option>
      </b-select>

      <b-select v-model="selectedPlayer">
        <option disabled value=''>Select a player</option>
        <option v-for="player in selectedTeam.players" v-bind:key="player">
          {{ player }}
        </option>
      </b-select>

      <p v-if="selectedTeam&&selectedPlayer">
        You selected a {{ selectedTeam.label }} and specifically {{ selectedPlayer }}.
      </p>

    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'StrikeEmOut',
  data() {
    return {
      msg: '',

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
