<template>
  <div class="info">
    <hr>
    <br>
    <h1>Er det så <i>vann</i>skelig?</h1>
    <br>
    <h2>VannSkli Oslo Vannrenseannlegg</h2>
    <br>
    <img src="../assets/vannrenseannlegg.jpg" style="border: 5px solid black" alt="VannSkli Oslo Vannrenseannlegg">
    <br>
    <br>
      <h2>FAQ</h2>
      <h3>Hvem er vi?</h3>
      <p>Vi renser vann slik at det er drikkbart for alle innen Oslo kommune.</p>
      <br>
      <h3>Hvor lenge har VannSkli vannrenseannlegg holdt på?</h3>
      <p>Byggingen av vannrenseannlegget begynte i 2003 og var ferdigstilt våren 2008.</p>
      <br>
      <h3>Hvor kan vi finne dere?</h3>
      <p>VannSkli vannrenseannlegg ligger i Mikroplastveien 3.</p>
      <ol style="line-height: 280%; list-style-type: none;">Dere kan også finne oss på følgende sosiale medier:
        <li>Instagram: <span style="color: blue">www.instagram.com/VannSkliWaterTreatmentFacility/?hl=en</span></li>
        <li>Youtube: <span style="color: blue">www.youtube.com/channel/VannSkliWaterTreatmentFacility12351245</span></li>
      </ol>
      <br>
      <br>
  </div>
</template>

<script>
import Hint from '../store/Hint'
export default {
  name: 'Info',
  created(){
    console.log(Hint);
  }
}
</script>
