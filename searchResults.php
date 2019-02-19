<html lang ="en">
<head>
<meta charset="UFT-8">
<meta http-equiv="X-UA-Compatible" content="IE-edge">
<meta name="viewport" content="width = device-width, initial-scale = 1">

<title>search results page</title>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


</head>

<body>

<div class="container">

<div class="page-header">

<div class="row">

    <div class="col-lg-2 col-med-2 col-sm-1 col-xs-1">
      <div>
         <h1>Philly Phoodies</h1>
         <form action='./searchResults.php' method='get'>
         <input type='text' name='searchEntry' id='searchEntry' value='<?php echo $_GET['searchEntry']; ?>' placeholder='Search' /></br>
         <div class="dropdown">

         <select class="dropdown1" name="price" id="price">
            <option value="$">$</option>
            <option value="$$">$$</option>
            <option value="$$$">$$$</option>
            <option value="$$$$">$$$$</option>
         </select>
         </br>
         <select class="dropdown2" name="distance" id="distance">
            <option value="1MileAway">1 Mile Away</option>
            <option value="3MileAway">3 Miles Away</option>
            <option value="5MileAway">5 Miles Away</option>
            <option value="7MileAway">7 Miles Away</option>
         </select>
         </br>
         <input type="submit" id="enter" value="Enter" />
      </div>
      </form>
    </div>
  </div>

    <div class="col-lg-1 col-med-1 col-sm-1 col-xs-1">

    </div>

    <div class="col-lg-9 col-med-9 col-sm-10 col-xs-10">
      <p>
        <h1>Results</h1>
      </br>

        <?php
           $searchEntry = $_GET['searchEntry'];
           $terms = explode(" ", $searchEntry);
           $query = "SELECT * FROM search WHERE ";
           $i=0;

           foreach ($terms as $each) {
             $i++;
             if ($i == 1)
                $query .= "keywords LIKE '%$each%' ";
             else
                $query .= "OR keywords LIKE '%$each%' ";
           }
           //connect to Datebase
           mysql_connect("localhost", "root", "");
           mysql_select_db("PhillyPhoodiesOfficial");

           $query = mysql_query($query);
           $numrows = mysql_num_rows($query);
           if ($numrows > 0) {

             while ($row = mysql_fetch_assoc($query)) {
               $id = $row['id'];
               $title = $row['title'];
               $description = $row['description'];
               $keywords = $row['keywords'];
               $address = $row['address'];
               $price = $row['price'];
               $link = $row['link'];

               echo "<h3><a href='$link'>$title</a></h3>
               $description<br /><br />";
             }

           }
           else
              echo "No results found for \"<br>$searchEntry</br>\"";

           //disconnect from Database
           mysql_close();

        ?>

     </p>

   </div>

</div>

</div>

</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
