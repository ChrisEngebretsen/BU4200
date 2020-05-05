<template>
  <div class="miljo">
    <hr>
    <h1>Miljømål og tips</h1>
    <h3 style="line-height:170%;text-decoration: underline;">Hver dag bruker en gjennomsnittlig nordmann 183 liter vann,<br>
      hvilke <span style="color: rgb(220,0,0)">konsekvenser</span> har dette for <span style="color: rgb(0,200,0)">miljøet?</span></h3>
    <h4 style="line-height:160%; ">Konsekvensene består av en undervurdert miljøbelastning, 
      <br> større kommunale energi- og strømavgifter,<br>
      store mengder kjemikalier, klimagassutslipp,<br>
      mikroplast og hormonforstyrrende stoffer, så vel som <br>
      et press på vannforsyningen i Oslo kommune.</h4>
      <br>
      <h3 style="line-height:120%;text-decoration: underline;">Hvilke tiltak kan gjøres for å redusere vannforbruket?</h3>
      <h4 style="line-height:120%">Det finnes flere tiltak en kan gjøre for å spare på vannet.</h4>
      <ol style="line-height:150%; list-style-type: none;">
        <li><span style="font-weight: bold;">Være bevisst på vannforbruket og unngå unødvendig svinn.</span></li>
        <li><span style="font-weight: bold;">Vask klær samlet og unngå å vaske klær separat.</span></li>
        <li><span style="font-weight: bold;">Prøv å samle regnvann og kok til rent drikkevann.</span></li>
        <li><span style="font-weight: bold;">Unngå å bruke vannspreder til å vanne blomsterbedd over lengre tid.</span></li>
      </ol>
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