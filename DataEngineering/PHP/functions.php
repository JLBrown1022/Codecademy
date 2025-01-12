<?php
function has2b(&$has2b, &$square) {
	// has2b($has2b, $square);
	for ($col = 0; $col <= 2; $col++) { // make $has2b unique
		$num = substr($square, $col, 1);
		if ($num != '*' && strlen($num) > 0) {
			$found = substr_count($has2b, $num); // find next $num
			if (!$found) $has2b .= $num;
		}
	}
}
function cantb (&$has2b, &$string, $this_row) {
	// cantb ($has2b, $string, $this_row);
	// remove characters in $row[s] from $string
	for ($col = 0; $col <= strlen($string); $col++) {
		$num = substr($this_row, $col, 1);
		if ($num != '*') {
			$string = str_replace($num, '', $string);
			$has2b = str_replace($num, '', $has2b);
		}
	}
}
function common (&$has2b, &$string) {
	// common ($has2b, $string);
	for ($x = 0; $x < strlen($has2b); $x++) {
		$num = substr($has2b, $x, 1);
		$string = str_replace($num, '', $string);
	}
}
function plus(&$plus, &$string) {
	// plus ($plus, $string);
	$plus = substr($string, 3);
	$string = substr($string, 0, 3);
}
function find_col ($square, $box, $row, &$find, $pos) {
	// $box = 0; $pos = 0; find_col ($square, $box, $row, $find, $pos);
	$find = '';
	for ($row = 0; $row <= 2; $row++) { // string the column numbers in $square
		$find .= substr($square[$box][$row], $pos, 1);
	}
	return $find;
}
function isnt (&$string, $this_row) {
	// isnt ($string, $this_row);
	// remove characters in $row[s] from $string
	for ($col = 0; $col <= strlen($this_row); $col++) {
		$num = substr($this_row, $col, 1);
		$string = str_replace($num, '', $string);
	}
}
function reset_string (&$_characters, &$string, &$has2b, &$x, &$plus) {
	// reset_string ($_characters, $string, $has2b, $x, $plus);
	$string = str_shuffle($_characters);
	$has2b = '';
	$plus = '';
	$x = 0;
}
function highMedLow ($high, $med, $low, $canbe) {
	// highMedLow ($low, $med, $high, &$canbe);
	
	if (strlen($canbe[$low]) >= 1) {
		for ($i = 0; $i < strlen($canbe[$low]); $i++) {
			$num = substr($canbe[$low], $i, 1);
			$found = substr_count($canbe[$med], $num);
			if ($found) $canbe[$low] = $num;
		}
	}
	
	$canbe[$med] = str_replace($canbe[$low], '', $canbe[$med]);
	
	if (strlen($canbe[$med]) >= 1) {
		for ($i = 0; $i < strlen($canbe[$med]); $i++) {
			$num = substr($canbe[$med], $i, 1);
			$found = substr_count($canbe[$high], $num);
			if ($found) $canbe[$med] = $num;
		}
	}
	
	$canbe[$high] = str_replace($canbe[$low], '', $canbe[$high]);
	$canbe[$high] = str_replace($canbe[$med], '', $canbe[$high]);

	$canbe[$high] = substr($canbe[$high], 0, 1);
}
function solve (&$square, &$string, &$plus, &$has2b, &$found, &$find, $box, $row) {
	// $box = 1; $row = 1; solve ($square, $string, $plus, $has2b, $found, $find, $box, $row);
	$x = 0; $y = 0; unset($canbe);
	
	for ($i = 0; $i < strlen($string); $i++) {
		for ($x = 0; $x <= 2; $x++) {
			$num = substr($string, $i, 1);
			$found = substr_count($find[$x], $num);
			if ($found == 0){
				$canbe[$x] .= $num;
			}
		}
	}
	$a = $canbe[0]; $b = $canbe[1]; $c = $canbe[2];
	
	if ($a >= $b && $b >= $c) $d = "012";
	if ($a >= $c && $c >= $b) $d = "021";
	if ($b >= $a && $a >= $c) $d = "102";
	if ($b >= $c && $c >= $a) $d = "120";
	if ($c >= $a && $a >= $b) $d = "201";
	if ($c >= $b && $b >= $a) $d = "210";

	
	switch ($d) {
		case "012" : 
			highMedLow (0, 1, 2, &$canbe);
			break;
		case "021" : 
			highMedLow (0, 2, 1, &$canbe);
			break;
		case "102" :
			highMedLow (1, 0, 2, &$canbe);
			break;
		case "120" :
			highMedLow (1, 2, 0, &$canbe);
			break;
		case "201" : 
			highMedLow (2, 0, 1, &$canbe);
			break;
		case "210" : 
			highMedLow (2, 1, 0, &$canbe);
			break;
	}
	for ($x = 0; $x <= 2; $x++) {
		if ($canbe[$x] == '') {
//			$canbe[$x] = '*';
			for ($i = 0; $i < strlen($plus); $i++) {
				$num = substr($plus, $i, 1);
				$found = substr_count($find[$x], $num);
				if ($found == 0){
					$canbe[$x] = $num; break;
				}
			}
		}
	}
	$square = $canbe[0] . $canbe[1] . $canbe[2];
}
?>