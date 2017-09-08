function Consonant(symbol,place,manner,voicing){
    this.symbol = symbol;
    this.place = place;
    this.manner = manner;
    this.voicing = voicing;
};

Consonant.prototype.getCategories = function(){
    return [this.place,this.manner,this.voicing];
};

Consonant.prototype.makeSpan = function() {
    return '<span id="' + consonants.indexOf(this) + '">' + this.symbol + '</span>';
};

var consonants = [
    new Consonant('m','bilabial','nasal','voiced'),
    new Consonant('n','alveolar','nasal','voiced'),
    new Consonant('ɳ','retroflex','nasal','voiced'),
    new Consonant('ɲ','palatal','nasal','voiced'),
    new Consonant('ŋ','velar','nasal','voiced'),
    new Consonant('ɴ','uvular','nasal','voiced'),
    new Consonant('p','bilabial','plosive','unvoiced'),
    new Consonant('b','bilabial','plosive','voiced'),
    new Consonant('t','alveolar','plosive','unvoiced'),
    new Consonant('d','alveolar','plosive','voiced'),
    new Consonant('ʈ','retroflex','plosive','unvoiced'),
    new Consonant('ɖ','retroflex','plosive','voiced'),
    new Consonant('c','palatal','plosive','unvoiced'),
    new Consonant('ɟ','palatal','plosive','voiced'),
    new Consonant('k','velar','plosive','unvoiced'),
    new Consonant('g','velar','plosive','voiced'),
    new Consonant('q','uvular','plosive','unvoiced'),
    new Consonant('ɢ','uvular','plosive','voiced'),
    new Consonant('ʔ','glottal','plosive','unvoiced'),
    new Consonant('f','labio-dental','fricative','unvoiced'),
    new Consonant('v','labio-dental','fricative','voiced'),
    new Consonant('s','alveolar','fricative','unvoiced'),
    new Consonant('z','alveolar','fricative','voiced'),
    new Consonant('ʂ','retroflex','fricative','unvoiced'),
    new Consonant('ʐ','retroflex','fricative','voiced'),
    new Consonant('ç','palatal','fricative','unvoiced'),
    new Consonant('ʝ','palatal','fricative','voiced'),
    new Consonant('x','velar','fricative','unvoiced'),
    new Consonant('ɣ','velar','fricative','voiced'),
    new Consonant('χ','uvular','fricative','unvoiced'),
    new Consonant('ʁ','uvular','fricative','voiced')
]

var places = ['bilabial','labio-dental','alveolar','retroflex','palatal','velar','uvular','glottal'];
var manners = ['nasal','plosive','fricative'];

function findAtIntersection(place, manner){
    var list = [];
    for(var i=0;i<consonants.length;i++){
        var consonant = consonants[i];
        if(consonant.place === place && consonant.manner === manner){
            list.push(consonant.makeSpan());
        }
    }
    return list;
};

function makeTable(){
    var string = '<thead><tr><td></td><td class="label ' + places.join('"></td><td class="label ') + '"></td></tr></thead><tbody>';
    for(var i=0; i<manners.length;i++){
        string += '<tr><td class="label ' + manners[i]+ '"></td>';
        for(var j=0; j<places.length; j++){
            string += '<td class="' + places[j] + ' ' + manners[i] + '">' + findAtIntersection(places[j],manners[i]).join() + '</td>';
        }
        string += '</tr>';
    }
    string += '</tbody>';
    return string;
};

function updateHighlightedClasses(){
    $('.highlight').removeClass('highlight');
    $('.added').each(function(){
        $(this).data().getCategories().forEach(function(category){
            $('.'+category).addClass('highlight');
        });
    });
};

$(document).ready(function(){
    $('table').append(makeTable());
    
    for(var i=0;i<consonants.length;i++){
        $('#'+i).data(consonants[i]);
        $('#'+i).removeAttr('id');
    }
    $('.label').each(function(){
        $(this).html($(this).attr('class').split(' ')[1]);
    });
    
    $('span').on('click',function(){
        $(this).toggleClass('added');
        updateHighlightedClasses();
    });
    
    $('.label').on('click',function(){
        var category = $(this).attr('class').split(' ')[1];
        if($(this).hasClass('highlight')){
            $('.'+category).removeClass('highlight');
            $('.'+category+'>span').removeClass('added');
            updateHighlightedClasses();
        } else {
            updateHighlightedClasses();
            $('.'+category).addClass('highlight');
        }
    });
    
    $('#expander').on('click',function(){
        if($(this).hasClass('collapsed')){
            $('td').show();
            $(this).removeClass('collapsed');
        } else {
            $('.label').each(function(){
                if(!$(this).hasClass('highlight')){
                    var category = $(this).attr('class').split(' ')[1]
                    $('.'+category).hide()
                }
            });
            $(this).addClass('collapsed');
        }
    });
});