<?php
class Path {

    private string $current_directory;

    function __construct(string $name_path) {
        $this->current_directory = $name_path;
    }

    public function getCurrentDirectory(): string
    {
        return $this->current_directory;
    }

    public function changeDirectory(string $directory_to_change_to) {
        $path_array = explode('/', $directory_to_change_to);
        $parent_directories_count = array_count_values($path_array)['..'];

        $current_directory = explode('/', $this->current_directory);
        array_splice($current_directory, -$parent_directories_count);
        if (end($path_array) != '..') {
            array_push($current_directory, end($path_array));
        }
        $new_current_directory = implode('/', $current_directory);

        $this->current_directory = $new_current_directory;
    }
}

?>