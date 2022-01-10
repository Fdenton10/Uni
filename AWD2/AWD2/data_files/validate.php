<?php
$xdoc = new DomDocument;
$xmlfile = 'data_188.xml';
$xmlschema = 'air-quality.xsd';

$xdoc -> Load($xmlfile);
if($xdoc ->schemaValidate($xmlschema)){
    echo ("$xmlfile is valid.\n");
}
else{
    echo("$xmlfile is invalid");
}
?>

