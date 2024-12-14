// Playlist Minimizing Functionality
const minimizeBtn = document.getElementById('minimizeBtn');
const playlistContainer = document.getElementById('playlist');
const nowPlayingSection = document.getElementById('nowPlaying');
const nowPlayingTitle = document.getElementById('nowPlayingTitle');
const nowPlayingImage = document.getElementById('nowPlayingImage');
const playingTitle = document.getElementById('playingTitle');
const playingImage = document.getElementById('playingImage');
const playlistControls = document.querySelector('.playlist-controls'); // Controls section

// Set playlist container to be visible and show now playing section on initial load
playlistContainer.style.display = 'block';  // Ensure playlist is maximized initially
nowPlayingSection.style.display = 'none';  // Optionally hide the detailed now playing section on initial load

minimizeBtn.addEventListener('click', () => {
    const isPlaylistVisible = playlistContainer.style.display !== 'none';
    
    if (isPlaylistVisible) {
        // Minimize playlist
        playlistContainer.style.display = 'none';
        nowPlayingSection.style.display = 'none'; // Hide detailed now playing
        minimizeBtn.textContent = '+'; // Change button to show expand option
        
        // Hide the image in controls when playlist is minimized
        playingImage.style.display = 'none'; // Hide image in controls
    } else {
        // Expand playlist
        playlistContainer.style.display = 'block';
        nowPlayingSection.style.display = 'none'; // Hide detailed now playing when playlist is expanded
        minimizeBtn.textContent = '-'; // Change button back to minimize option

        // Hide the image in controls when the playlist is expanded (maximized)
        playingImage.style.display = 'none'; // Hide image in controls
    }
});

// Playlist Controls (Play, Pause, Next, Previous, Volume)
const audioPlayers = document.querySelectorAll('.audio-player');
let currentSongIndex = 0;
let isPlaying = false;
let currentAudio = audioPlayers[currentSongIndex];

// Update "Now Playing" info when a new song starts playing
function updateNowPlayingInfo() {
    if (isPlaying) {
        const songName = currentAudio.dataset.songName;
        const songImage = currentAudio.dataset.songImage;
        
        // Update the main info section (Title above image)
        playingTitle.textContent = songName;
        playingTitle.style.display = 'block'; // Ensure the title is visible
        playingImage.src = songImage;
        playingImage.style.display = 'block'; // Show the image when a song is playing

        // Set the image width to 150px when playing
        playingImage.style.width = '150px'; // Image width during playback
        playingImage.style.height = ''; // Automatically adjust height to maintain aspect ratio

        // Update the detailed now playing section
        nowPlayingTitle.textContent = songName;
        nowPlayingTitle.style.display = 'block'; // Ensure the title is visible
        nowPlayingImage.src = songImage;
        nowPlayingImage.style.display = 'block'; // Show the image when a song is playing
        nowPlayingImage.style.width = '150px'; // Set width for the detailed view
        nowPlayingImage.style.height = ''; // Automatically adjust height to maintain aspect ratio
    } else {
        // Clear the now playing info if no song is playing
        playingTitle.textContent = '';
        playingTitle.style.display = 'none'; // Hide the title when no song is playing
        playingImage.src = '';
        playingImage.style.display = 'none'; // Hide the image when no song is playing
        
        nowPlayingTitle.textContent = '';
        nowPlayingTitle.style.display = 'none'; // Hide the title when no song is playing
        nowPlayingImage.src = '';
        nowPlayingImage.style.display = 'none'; // Hide the image when no song is playing

        // Reset size when no song is playing
        playingImage.style.width = ''; // Reset width
        playingImage.style.height = ''; // Reset height
        nowPlayingImage.style.width = ''; // Reset width
        nowPlayingImage.style.height = ''; // Reset height
    }
}

// Play/Pause functionality
const playPauseButton = document.getElementById('playPauseBtn');
playPauseButton.addEventListener('click', () => {
    if (isPlaying) {
        currentAudio.pause();
        playPauseButton.innerText = 'Play';
    } else {
        currentAudio.play();
        playPauseButton.innerText = 'Pause';
    }
    isPlaying = !isPlaying;
    updateNowPlayingInfo(); // Update now playing info whenever song starts
});

// Next song functionality
const nextButton = document.getElementById('nextBtn');
nextButton.addEventListener('click', () => {
    if (currentSongIndex < audioPlayers.length - 1) {
        currentAudio.pause();
        currentSongIndex++;
        currentAudio = audioPlayers[currentSongIndex];
        currentAudio.play();
        isPlaying = true;
        playPauseButton.innerText = 'Pause';
        updateNowPlayingInfo(); // Update now playing info
    }
});

// Previous song functionality
const prevButton = document.getElementById('prevBtn');
prevButton.addEventListener('click', () => {
    if (currentSongIndex > 0) {
        currentAudio.pause();
        currentSongIndex--;
        currentAudio = audioPlayers[currentSongIndex];
        currentAudio.play();
        isPlaying = true;
        playPauseButton.innerText = 'Pause';
        updateNowPlayingInfo(); // Update now playing info
    }
});

// Volume control functionality
const volumeControl = document.getElementById('volumeControl');
volumeControl.addEventListener('input', () => {
    currentAudio.volume = volumeControl.value;
});

// Auto-switch to next song when current one ends
currentAudio.addEventListener('ended', () => {
    if (currentSongIndex < audioPlayers.length - 1) {
        currentSongIndex++;
        currentAudio = audioPlayers[currentSongIndex];
        currentAudio.play();
        isPlaying = true;
        playPauseButton.innerText = 'Pause';
        updateNowPlayingInfo(); // Update now playing info
    }
});
