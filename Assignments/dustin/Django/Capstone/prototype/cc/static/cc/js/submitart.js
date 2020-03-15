function toggle(button)
{
    if(document.getElementById("sinmultselect").value=="Collection"){
        document.getElementById("sinmultselect").value="Single";
        sin = document.getElementById("single_art");
        mult = document.getElementById("collection_art")
        sin.style.display = "block";
        mult.style.display = "none";
    }
    else if(document.getElementById("sinmultselect").value=="Single"){
        document.getElementById("sinmultselect").value="Collection";
        sin = document.getElementById("single_art");
        mult = document.getElementById("collection_art")
        sin.style.display = "none";
        mult.style.display = "block";
    }
};

function toggle1(button)
{
    if(document.getElementById("1").value=="Image"){
        document.getElementById("1").value="Text";
        image = document.getElementById("imageupload1");
        text = document.getElementById("textupload1");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("1").value=="Text"){
        document.getElementById("1").value="Image";
        image = document.getElementById("imageupload1");
        text = document.getElementById("textupload1");
        mce = document.getElementById("tinyText1")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile1 = function(event) {
    var output1 = document.getElementById('output1');
    output1.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText1',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function toggle2(button)
{
    if(document.getElementById("2").value=="Image"){
        document.getElementById("2").value="Text";
        image = document.getElementById("imageupload2");
        text = document.getElementById("textupload2");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("2").value=="Text"){
        document.getElementById("2").value="Image";
        image = document.getElementById("imageupload2");
        text = document.getElementById("textupload2");
        mce = document.getElementById("tinyText2");
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile2 = function(event) {
    var output2 = document.getElementById('output2');
    output2.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText2',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function showEntryTwo(button) 
{
    showEntryTwo = document.getElementById("showEntry2");
    entryTwo = document.getElementById("entryTwo");
    entryTwo.style.display = "block";
};

function toggle3(button)
{
    if(document.getElementById("3").value=="Image"){
        document.getElementById("3").value="Text";
        image = document.getElementById("imageupload3");
        text = document.getElementById("textupload3");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("3").value=="Text"){
        document.getElementById("3").value="Image";
        image = document.getElementById("imageupload3");
        text = document.getElementById("textupload3");
        mce = document.getElementById("tinyText3")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile3 = function(event) {
    var output3 = document.getElementById('output3');
    output3.src = URL.createObjectURL(event.target.files[0]);
}

tinymce.init({
    selector: '#tinyText3',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function showEntryThree(button) 
{
    showEntryTwo = document.getElementById("showEntry3");
    entryThree = document.getElementById("entryThree");
    entryThree.style.display = "block";
};

function toggle4(button)
{
    if(document.getElementById("4").value=="Image"){
        document.getElementById("4").value="Text";
        image = document.getElementById("imageupload4");
        text = document.getElementById("textupload4");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("4").value=="Text"){
        document.getElementById("4").value="Image";
        image = document.getElementById("imageupload4");
        text = document.getElementById("textupload4");
        mce = document.getElementById("tinyText4")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile4 = function(event) {
    var output4 = document.getElementById('output4');
    output4.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText4',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function showEntryFour(button) 
{
    showEntryFour = document.getElementById("showEntry4");
    entryFour = document.getElementById("entryFour");
    entryFour.style.display = "block";
};

function toggle5(button)
{
    if(document.getElementById("5").value=="Image"){
        document.getElementById("5").value="Text";
        image = document.getElementById("imageupload5");
        text = document.getElementById("textupload5");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("5").value=="Text"){
        document.getElementById("5").value="Image";
        image = document.getElementById("imageupload5");
        text = document.getElementById("textupload5");
        mce = document.getElementById("tinyText5")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile5 = function(event) {
    var output5 = document.getElementById('output5');
    output5.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText5',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function showEntryFive(button) 
{
    showEntryFive = document.getElementById("showEntry5");
    entryFive = document.getElementById("entryFive");
    entryFive.style.display = "block";
};

function toggle6(button)
{
    if(document.getElementById("6").value=="Image"){
        document.getElementById("6").value="Text";
        image = document.getElementById("imageupload6");
        text = document.getElementById("textupload6");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("6").value=="Text"){
        document.getElementById("6").value="Image";
        image = document.getElementById("imageupload6");
        text = document.getElementById("textupload6");
        mce = document.getElementById("tinyText6")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";
    }
};

var loadFile6 = function(event) {
    var output6 = document.getElementById('output6');
    output6.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText6',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});

function showEntrySix(button) 
{
    showEntrySix = document.getElementById("showEntry6");
    entrySix = document.getElementById("entrySix");
    entrySix.style.display = "block";
};

function toggle7(button)
{
    if(document.getElementById("7").value=="Image"){
        document.getElementById("7").value="Text";
        image = document.getElementById("imageupload7");
        text = document.getElementById("textupload7");
        image.style.display = "none";
        text.style.display = "block";
    }
    else if(document.getElementById("7").value=="Text"){
        document.getElementById("7").value="Image";
        image = document.getElementById("imageupload7");
        text = document.getElementById("textupload7");
        mce = document.getElementById("tinyText7")
        image.style.display = "block";
        text.style.display = "none";
        mce.style.display= "none";

    }
};

var loadFile7 = function(event) {
    var output7 = document.getElementById('output7');
    output7.src = URL.createObjectURL(event.target.files[0]);
};

tinymce.init({
    selector: '#tinyText7',
    plugins: 'a11ychecker advcode casechange formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker',
    toolbar: 'casechange checklist code',
    toolbar_mode: 'floating',
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
    skin: 'oxide-dark',
    menubar: 'edit insert view format table tools help'
});
