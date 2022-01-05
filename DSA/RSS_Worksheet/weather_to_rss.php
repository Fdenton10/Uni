<?php 
require("wdllib.php"); 

//main 
  $site = $_REQUEST["site"]; 
  $rawdatafile = $site . "/clientraw.txt"; 
  $csv = file_get_contents($rawdatafile); 
  $data = explode(' ',$csv); 
    
// generate the RSS  
print <<<EOT
<?xml version="1.0"?>  
<rss version="2.0"> 
  <channel> 
      <title>{$data[STATION]}</title> 
      <link>{$site}</link> 
      <item> 
         <title>Weather at {$data[TIMEHH]}:{$data[TIMEMM]}</title> 
         <description> {$data[SUMMARY]} . Wind {$data[WINDSPEED]} knots from {$data[WINDDIRECTION]}  degrees. Temperature {$data[TEMPERATURE]} &#0176;C. </description> 
      </item> 
  </channel> 
 </rss> 
EOT;
?>