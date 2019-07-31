<?php
$cmd = "python3 test.py";

exec(escapeshellcmd($cmd), $output, $status);

if ($status) echo "Exec Command Failed";
else
{
		echo "<pre>";
		foreach($output as $line) echo htmlspecialchars("$line\n");
		echo "</pre>";
}
/*
echo <<<_END
<html><head><title>PHP Form Upload</title></head><body>
<form method='post' action='index.php' enctype='multipart/gorm-data'>
Select File: <input type='file' name='filename' size='10'>
<input type='submit' value='Upload'>
</form>
_END;

if ($_FILES)
{
		$name = $FILES['filename']['name'];
		move_uploaded_file($_FILES['filename']['tmp_name'], $name);
		echo "Uploaded image '$name'<br /><img src='$name'>";
}

echo "</body></html>";

/*
echo file_get_contents("http://oreilly.com");
/*
$fh = fopen("phpt.txt", 'r') or die("Failed to create file");


$text1 = fgets($fh) or die("Could not write to file");
$text2 = fread($fh, 100);
fclose($fh);
echo "<pre>";
echo $text1;
echo "<br>";
echo $text2;
echo "</pre>";
$p1 = array("Copier", "Inkjet", "Laser", "Photo");

echo "p1 element: " . $p1[2] . "<br>";

$p2 = array("copier" => "Copier & Multipurpose",
			"inkjet" => "Inkjet Printer",
			"laser" => "LAser Printer",
			"photo" => "Photographic Paper");

echo "p2 element: " . $p2["inkjet"] . "<br>";

foreach ($p1 as $item)
{
		echo "$item<br>";
}

$j = 0;
foreach ($p2 as $ite)
{
		echo "$j: $ite<br>";
		$j++;
}

foreach ($p2 as $it => $des)
{
		echo "$it: $des<br>";
}

echo $copier;
extract($p2);
echo $copier;

echo date(DATE_RSS, time());
$a1 = "WILLIAM";
$a2 = "xxGHW";
$a3 = "kjYDcv";

echo $a1 . " " . $a2 . " " . $a3 . "<br>";
$nn = fix_names($a1, $a2, $a3);
echo $nn[0] . " " . $nn[1] . " " . $nn[2] . "<br>";
echo $a1 . " " . $a2 . " " . $a3 . "<br>";

function fix_names($n1, $n2, $n3)
{
		$n1 = ucfirst(strtolower($n1));
		$n2 = ucfirst(strtolower($n2));
		$n3 = ucfirst(strtolower($n3));
		return array($n1, $n2, $n3);
}
echo phpversion();
$object = new User;
print_r($object);
echo "<br>";
$object->name = "Joe";
$object->password = "mypass";
print_r($object);
echo "<br>";
$object->save_user();

class User
{
		public $name, $password;
		function save_user()
		{
				echo "Save User Code Gose Here.";
		}
}
 */
?>

