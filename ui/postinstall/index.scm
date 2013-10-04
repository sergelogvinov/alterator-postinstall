(document:surround "/std/frame")

(label "PostInstall")
(edit name "method")
(edit name "url")
(edit name "cmd")
(button "Write")

(frame:buttons-view
 (button (_ "Quit") (when clicked (document:end))))
