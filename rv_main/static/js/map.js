// We need to use JS to make a map of games

// 
function rvAddGame(game, position){
    $('#mapContainer').append('<div class="game"></div>');
    $('.game').text = getGameName(game);
    $('.game').id = game;
}
