<template>
  <div class="kontakt">
    <hr>
    <h1>Ønsker du videre informasjon?</h1>
    <input type="text" style="border:solid 2px black" placeholder="Din Email">
    <p>Vi tar kontakt med deg snart</p>
  </div>
</template>
<script>
import Hint from '../store/Hint'
export default {
  created(){
    console.log(Hint);
  }
}
</script>