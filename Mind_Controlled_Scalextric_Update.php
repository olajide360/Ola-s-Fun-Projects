<?php

$con = mysql_connect('localhost','root','root');
mysql_select_db('PerformanceDataTable',$con);

$query = "SELECT * from table_main ORDER BY SerialNumber DESC LIMIT 1";

$result = mysql_query( $query);
while( $row =mysql_fetch_array( $result, MYSQL_NUM))
{
 $attvalue = $row['1'];
 $medvalue = $row['2'];
 $deltavalue = $row['3'];
 $thetavalue = $row['4'];
 $lowalphavalue = $row['5'];
 $highalphavalue = $row['6'];
 $lowbetavalue = $row['7'];
 $highbetavalue = $row['8'];
 $lowgammavalue = $row['9'];
 $midgammavalue = $row['10'];
}


$arrr = array ("attvalue"=>$attvalue,              "medvalue"=>$medvalue,             "deltavalue"=>$deltavalue,           $thetavalue=> $thetavalue ,
              "lowalphavalue" => $lowalphavalue  ,      "highalphavalue" => $highalphavalue ,  "lowbetavalue" =>  $lowbetavalue    ,   "highbetavalue" => $highbetavalue ,
              "lowgammavalue" => $lowgammavalue  ,      "midgammavalue" => $midgammavalue    );

$value = max($arrr);

$d= ceil(($deltavalue/$value )* 100);
$t= ceil(($thetavalue/$value )* 100);
$la= ceil(($lowalphavalue/$value )* 100);
$ha= ceil(($highalphavalue/$value )* 100);
$lb= ceil(($lowbetavalue/$value )* 100);
$hb= ceil(($highbetavalue/$value )* 100);
$lg= ceil(($lowgammavalue/$value )* 100);
$mg= ceil(($midgammavalue/$value )* 100);



$arr = array ("attvalue"=>$attvalue,              "medvalue"=>$medvalue,             "deltavalue"=>$deltavalue,           "thetavalue" => $thetavalue ,
              "lowalphavalue" => $lowalphavalue  ,      "highalphavalue" => $highalphavalue ,  "lowbetavalue" =>  $lowbetavalue    ,   "highbetavalue" => $highbetavalue ,
              "lowgammavalue" => $lowgammavalue  ,      "midgammavalue" => $midgammavalue ,
		"d" => $d,  "t" => $t,  "la"=>$la,   "ha" => $ha,   "lb" => $lb,   "hb" => $hb,   "lg" => $lg,    "mg" => $mg 
   );

echo json_encode($arr)


?>
