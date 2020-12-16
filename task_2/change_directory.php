<?php
class Path {

    private string $current_directory;

    function __construct(string $name_path) { $this->current_directory = $name_path; }

    public function getCurrentDirectory(): string { return $this->current_directory; }

    public function changeDirectory(string $directory_change) {
        $new_directory = explode('/', $this->current_directory);
        $last = $this->extractLastElementInPath($directory_change);

        array_splice($new_directory, -$this->extractNumberOfParentDirectories($directory_change));
        if ($last != "..") array_push($new_directory, $last);

        $this->current_directory = implode('/', $new_directory);
    }

    private function extractNumberOfParentDirectories(string $directory): int {
        $directory_as_array = explode('/', $directory);
        $parent_directories_count = array_count_values($directory_as_array)['..'];
        return $parent_directories_count;
    }

    private function extractLastElementInPath(string $directory) {
        $directory_as_array = explode('/', $directory);
        $last_element = end($directory_as_array);
        return $last_element;
    }
}

?>