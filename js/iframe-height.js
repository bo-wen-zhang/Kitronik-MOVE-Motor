document.addEventListener("DOMContentLoaded", function() {
    function changeHeight() {
        iframes = document.getElementsByClassName("iframe");
        for (let i = 0; i < iframes.length; i++) {
            const cloneDiv = iframes[i].cloneNode(true);
 
            cloneDiv.style.visibility = 'hidden'; // Hide the clone from view
            cloneDiv.style.overflow = 'hidden'; // Ensure overflow is hidden
            cloneDiv.style.position = 'absolute';
            cloneDiv.style.width = '100%';
            cloneDiv.style.height = '100%';

            // Append the clone to the document body
            document.body.appendChild(cloneDiv);

            // Calculate the height without scrollbar
            const heightWithoutScrollbar = cloneDiv.clientHeight;

            // Remove the clone from the document body
            document.body.removeChild(cloneDiv);
            console.log(heightWithoutScrollbar)
            console.log(iframes[i].clientHeight)
            iframes[i].height = heightWithoutScrollbar + 'px'
            iframes[i].style.width = '100%';
        }
    }
    changeHeight();
})