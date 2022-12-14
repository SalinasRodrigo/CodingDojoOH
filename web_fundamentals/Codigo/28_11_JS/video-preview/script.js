function over(element) {
    
    element.play();
    element.muted=true
    element.playbackRate=2.0;
}
    
function out(element) {
    element.pause(); 
    element.currentTime=0;
}


