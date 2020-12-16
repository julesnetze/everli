<?php

use PHPUnit\Framework\TestCase;

require('change_directory.php');

class ChangeDirectoryTest extends TestCase
{
    public function testOneParentDirectoryUp() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('..');

        $this->assertSame('/a/b/c', $path->getCurrentDirectory());
    }

    public function testOneParentDirectoryUpAndChangeDirectory() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('../x');

        $this->assertSame('/a/b/c/x', $path->getCurrentDirectory());
    }

    public function testTwoParentDirectoriesUpAndChangeDirectory() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('../../x');

        $this->assertSame('/a/b/x', $path->getCurrentDirectory());
    }

    public function testFourParentDirectoriesUpAndChangeDirectory() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('../../../../x');

        $this->assertSame('/x', $path->getCurrentDirectory());
    }

    public function testThreeParentDirectoriesUpAndTwoDirectoryChanges() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('../../x/../z');

        $this->assertSame('/a/b/z', $path->getCurrentDirectory());
    }

    public function testTwoParentDirectoriesUpAndTwoDirectoryChanges() {
        $path = new Path('/a/b/c/d');

        $path->changeDirectory('../../x/z');

        $this->assertSame('/a/b/x/z', $path->getCurrentDirectory());
    }
}
?>