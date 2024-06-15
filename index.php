<html>
<body>
<?php
$c = 0;
foreach (scandir("img",SCANDIR_SORT_DESCENDING) as $img)
{
	if ( $img === "." || $img === "..")
	{
		continue;
	}
	echo "<img src=\"img/".$img."\" width=400/> ";
	$c += 1;
	if ($c % 3 == 0) 
	{
		echo "<br/>";
	}
}
?>
<script>
setTimeout(() => 
{
	document.location.reload();
},15000);
</script>
</body>
</html>
