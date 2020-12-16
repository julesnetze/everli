<?php
class Path {

    private string $current_directory;

    function __construct(string $name_path) { $this->current_directory = $name_path; }

    public function getCurrentDirectory(): string { return $this->current_directory; }

    public function changeDirectory(string $directory_change) {
        $new_directory = explode('/', $this->current_directory);    

        foreach (explode('/', $directory_change) as $element) {
            if ($element == '..') {
                array_pop($new_directory);  
            } else {
                array_push($new_directory, $element);
            }
        }

        $this->current_directory = implode('/', $new_directory);
    }
}

?>