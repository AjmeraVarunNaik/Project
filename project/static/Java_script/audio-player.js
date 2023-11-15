const audioPlayer = document.getElementById('audio-player');
const previousButton = document.getElementById('previous');
const nextButton = document.getElementById('next');
const shuffleButton = document.getElementById('shuffle');
const currentSong = document.getElementById('current-song');
const songList = document.getElementById('song-list');
const songs = Array.from(document.querySelectorAll('#song-list li'));

let currentSongIndex = 0;

function loadSong(index) {
    audioPlayer.src = `/audio/${songs[index].getAttribute('data-src')}`;
    currentSong.textContent = `Now Playing: ${songs[index].textContent}`;
    audioPlayer.load();
    audioPlayer.play();
}

function playNextSong() {
    currentSongIndex = (currentSongIndex + 1) % songs.length;
    loadSong(currentSongIndex);
}

function shuffleSongs() {
    const shuffledIndexes = songs.map((song, index) => index);
    for (let i = shuffledIndexes.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledIndexes[i], shuffledIndexes[j]] = [shuffledIndexes[j], shuffledIndexes[i]];
    }
    currentSongIndex = shuffledIndexes.indexOf(currentSongIndex);
    loadSong(currentSongIndex);
}

songs.forEach((song, index) => {
    song.addEventListener('click', () => {
        currentSongIndex = index;
        loadSong(currentSongIndex);
    });
});

previousButton.addEventListener('click', () => {
    currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
    loadSong(currentSongIndex);
});

nextButton.addEventListener('click', () => {
    playNextSong();
});

audioPlayer.addEventListener('ended', () => {
    playNextSong();
});

shuffleButton.addEventListener('click', () => {
    shuffleSongs();
});

loadSong(currentSongIndex);
