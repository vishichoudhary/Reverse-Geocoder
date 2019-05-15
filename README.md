# Input format

like it ``'28.657776,77.289506'`` if only one coordinate is there

else like ``['28.657776,77.289506','28.657876,77.289606']`` if multiple coordinates are there

Please  mind the spaces and ``'`` characters, Input string has been parsed by considering these two cases;


# Cache
Used sqlite3 for caching

# Coordinates to location mapping

I have used md5 to generate a random address from given coordinate