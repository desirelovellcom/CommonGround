import pygame
import random
import math
import json
from typing import List, Tuple, Dict
from dataclasses import dataclass
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
GRID_WIDTH = 12
GRID_HEIGHT = 20
BLOCK_SIZE = 30
GRID_X = 50
GRID_Y = 100

# Pastel colors for gradient backgrounds
PASTEL_COLORS = {
    'foundation': (255, 182, 193),  # Light pink
    'culture': (173, 216, 230),     # Light blue
    'personal': (144, 238, 144),    # Light green
    'agents': (221, 160, 221),      # Plum
    'champions': (255, 218, 185),   # Peach
    'coins': (255, 255, 224),       # Light yellow
    'governance': (230, 230, 250)   # Lavender
}

class ComponentType(Enum):
    FOUNDATION_COIN = "Foundation Coin"
    II_AGENT = "II-Agent"
    NATIONAL_CHAMPION = "National Champion"
    ANCHOR_SET = "Anchor-Set"
    CULTURE_CREDIT = "Culture Credit"
    GUARDIAN_SENTINEL = "Guardian Sentinel"
    ORACLE_COUNCIL = "Oracle Council"

@dataclass
class GameBlock:
    x: int
    y: int
    component_type: ComponentType
    color: Tuple[int, int, int]
    info: str
    shape: List[List[int]]

class CommonGroundGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("CommonGround - Intelligent Internet Protocol")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 18)
        
        # Game state
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_block = None
        self.next_blocks = []
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = 500  # milliseconds
        
        # UI state
        self.selected_component = None
        self.info_panel_scroll = 0
        
        # Component definitions
        self.component_info = {
            ComponentType.FOUNDATION_COIN: {
                "description": "Intelligence-backed currency minted through Proof-of-Benefit",
                "details": "Fixed cap of 21M coins. Halves every 2 epochs. Backed by verifiable public benefit.",
                "color": PASTEL_COLORS['coins'],
                "shape": [[1, 1], [1, 1]]  # Square
            },
            ComponentType.II_AGENT: {
                "description": "Sovereign AI assistant bound to non-custodial wallet",
                "details": "Partner, Principal, and Associate hierarchy. Fully open-source with private key control.",
                "color": PASTEL_COLORS['agents'],
                "shape": [[1, 1, 1], [0, 1, 0]]  # T-shape
            },
            ComponentType.NATIONAL_CHAMPION: {
                "description": "Validator franchise running large compute clusters",
                "details": "BFT consensus with <300ms latency. Guarantees daily UAI quota for citizens.",
                "color": PASTEL_COLORS['champions'],
                "shape": [[1, 0, 1], [1, 1, 1]]  # U-shape
            },
            ComponentType.ANCHOR_SET: {
                "description": "Merkle roots of datasets and models on-chain",
                "details": "Tamper-evident provenance. Auditable training data with license verification.",
                "color": PASTEL_COLORS['foundation'],
                "shape": [[1, 1, 1, 1]]  # Line
            },
            ComponentType.CULTURE_CREDIT: {
                "description": "Jurisdiction-specific currency respecting local policy",
                "details": "FC-backed with reserve requirements. Enables data residency compliance.",
                "color": PASTEL_COLORS['culture'],
                "shape": [[1, 1, 0], [0, 1, 1]]  # Z-shape
            },
            ComponentType.GUARDIAN_SENTINEL: {
                "description": "AI agents monitoring network health and compliance",
                "details": "Sentinels, Advisers, and Implementers. Automatic rotation every 6 months.",
                "color": PASTEL_COLORS['governance'],
                "shape": [[0, 1, 1], [1, 1, 0]]  # S-shape
            },
            ComponentType.ORACLE_COUNCIL: {
                "description": "15-seat governance body using Common-Ground protocol",
                "details": "Parameter tuning through AI agent orchestration. 30-day grace period for changes.",
                "color": PASTEL_COLORS['governance'],
                "shape": [[1, 0, 0], [1, 1, 1]]  # L-shape
            }
        }
        
        self.generate_next_blocks()
        self.spawn_new_block()
        
    def create_gradient_surface(self, width: int, height: int, color1: Tuple[int, int, int], color2: Tuple[int, int, int]) -> pygame.Surface:
        """Create a gradient surface for memory efficiency"""
        surface = pygame.Surface((width, height))
        for y in range(height):
            ratio = y / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            pygame.draw.line(surface, (r, g, b), (0, y), (width, y))
        return surface
    
    def generate_next_blocks(self):
        """Generate next blocks queue"""
        components = list(ComponentType)
        self.next_blocks = [random.choice(components) for _ in range(3)]
    
    def spawn_new_block(self):
        """Spawn a new falling block"""
        if not self.next_blocks:
            self.generate_next_blocks()
            
        component_type = self.next_blocks.pop(0)
        self.next_blocks.append(random.choice(list(ComponentType)))
        
        info = self.component_info[component_type]
        self.current_block = GameBlock(
            x=GRID_WIDTH // 2 - 1,
            y=0,
            component_type=component_type,
            color=info['color'],
            info=info['description'],
            shape=info['shape']
        )
    
    def can_move(self, dx: int, dy: int, shape: List[List[int]] = None) -> bool:
        """Check if current block can move in given direction"""
        if not self.current_block:
            return False
            
        shape = shape or self.current_block.shape
        new_x = self.current_block.x + dx
        new_y = self.current_block.y + dy
        
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = new_x + col_idx
                    y = new_y + row_idx
                    
                    if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT:
                        return False
                    if y >= 0 and self.grid[y][x] is not None:
                        return False
        return True
    
    def place_block(self):
        """Place current block in grid"""
        if not self.current_block:
            return
            
        for row_idx, row in enumerate(self.current_block.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = self.current_block.x + col_idx
                    y = self.current_block.y + row_idx
                    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                        self.grid[y][x] = self.current_block
        
        self.check_lines()
        self.spawn_new_block()
    
    def check_lines(self):
        """Check for completed lines and clear them"""
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y][x] is not None for x in range(GRID_WIDTH)):
                lines_to_clear.append(y)
        
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [None for _ in range(GRID_WIDTH)])
        
        if lines_to_clear:
            self.lines_cleared += len(lines_to_clear)
            self.score += len(lines_to_clear) * 100 * self.level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(50, 500 - (self.level - 1) * 50)
    
    def rotate_shape(self, shape: List[List[int]]) -> List[List[int]]:
        """Rotate shape 90 degrees clockwise"""
        return [[shape[len(shape) - 1 - j][i] for j in range(len(shape))] 
                for i in range(len(shape[0]))]
    
    def draw_gradient_background(self):
        """Draw gradient background"""
        # Create main gradient
        gradient = self.create_gradient_surface(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            (20, 20, 40), (5, 5, 15)
        )
        self.screen.blit(gradient, (0, 0))
        
        # Add subtle pattern
        for i in range(0, WINDOW_WIDTH, 100):
            for j in range(0, WINDOW_HEIGHT, 100):
                alpha = int(20 * math.sin(i * 0.01) * math.cos(j * 0.01))
                if alpha > 0:
                    overlay = pygame.Surface((50, 50))
                    overlay.set_alpha(alpha)
                    overlay.fill((100, 50, 150))
                    self.screen.blit(overlay, (i, j))
    
    def draw_grid(self):
        """Draw game grid"""
        # Grid background
        grid_surface = pygame.Surface((GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE))
        grid_surface.set_alpha(50)
        grid_surface.fill((100, 100, 150))
        self.screen.blit(grid_surface, (GRID_X, GRID_Y))
        
        # Grid lines
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(self.screen, (80, 80, 120), 
                           (GRID_X + x * BLOCK_SIZE, GRID_Y),
                           (GRID_X + x * BLOCK_SIZE, GRID_Y + GRID_HEIGHT * BLOCK_SIZE))
        
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, (80, 80, 120),
                           (GRID_X, GRID_Y + y * BLOCK_SIZE),
                           (GRID_X + GRID_WIDTH * BLOCK_SIZE, GRID_Y + y * BLOCK_SIZE))
    
    def draw_block(self, block: GameBlock, offset_x: int = 0, offset_y: int = 0):
        """Draw a game block"""
        for row_idx, row in enumerate(block.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x = GRID_X + (block.x + col_idx + offset_x) * BLOCK_SIZE
                    y = GRID_Y + (block.y + row_idx + offset_y) * BLOCK_SIZE
                    
                    # Draw block with gradient effect
                    rect = pygame.Rect(x + 1, y + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2)
                    
                    # Main color
                    pygame.draw.rect(self.screen, block.color, rect)
                    
                    # Highlight
                    highlight_color = tuple(min(255, c + 30) for c in block.color)
                    pygame.draw.rect(self.screen, highlight_color, 
                                   (x + 1, y + 1, BLOCK_SIZE - 2, 3))
                    
                    # Shadow
                    shadow_color = tuple(max(0, c - 30) for c in block.color)
                    pygame.draw.rect(self.screen, shadow_color,
                                   (x + 1, y + BLOCK_SIZE - 4, BLOCK_SIZE - 2, 3))
                    
                    # Component type text
                    if BLOCK_SIZE > 25:
                        text = self.small_font.render(block.component_type.value[:3], True, (0, 0, 0))
                        text_rect = text.get_rect(center=(x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2))
                        self.screen.blit(text, text_rect)
    
    def draw_placed_blocks(self):
        """Draw all placed blocks in grid"""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    block = self.grid[y][x]
                    # Create temporary block for drawing
                    temp_block = GameBlock(x, y, block.component_type, block.color, block.info, [[1]])
                    self.draw_block(temp_block)
    
    def draw_ui(self):
        """Draw user interface elements"""
        title = self.title_font.render("CommonGround Protocol", True, (255, 255, 255))
        self.screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 10))
        
        # Score panel
        score_x = GRID_X + GRID_WIDTH * BLOCK_SIZE + 20
        score_y = GRID_Y
        
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (score_x, score_y))
        
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.blit(level_text, (score_x, score_y + 30))
        
        lines_text = self.font.render(f"Lines: {self.lines_cleared}", True, (255, 255, 255))
        self.screen.blit(lines_text, (score_x, score_y + 60))
        
        # Next blocks
        next_y = score_y + 100
        next_title = self.font.render("Next Components:", True, (255, 255, 255))
        self.screen.blit(next_title, (score_x, next_y))
        
        for i, component_type in enumerate(self.next_blocks[:3]):
            info = self.component_info[component_type]
            color = info['color']
            
            # Draw preview block
            preview_y = next_y + 30 + i * 60
            pygame.draw.rect(self.screen, color, (score_x, preview_y, 40, 20))
            
            # Component name
            name_text = self.small_font.render(component_type.value, True, (255, 255, 255))
            self.screen.blit(name_text, (score_x + 50, preview_y))
        
        # Info panel
        info_y = next_y + 200
        if self.selected_component:
            info = self.component_info[self.selected_component]
            
            info_title = self.font.render("Component Info:", True, (255, 255, 255))
            self.screen.blit(info_title, (score_x, info_y))
            
            name_text = self.font.render(self.selected_component.value, True, info['color'])
            self.screen.blit(name_text, (score_x, info_y + 30))
            
            # Description (wrapped)
            desc_lines = self.wrap_text(info['description'], 300)
            for i, line in enumerate(desc_lines):
                desc_text = self.small_font.render(line, True, (200, 200, 200))
                self.screen.blit(desc_text, (score_x, info_y + 60 + i * 20))
            
            # Details (wrapped)
            detail_lines = self.wrap_text(info['details'], 300)
            for i, line in enumerate(detail_lines):
                detail_text = self.small_font.render(line, True, (180, 180, 180))
                self.screen.blit(detail_text, (score_x, info_y + 120 + i * 20))
        
        # Controls
        controls_y = WINDOW_HEIGHT - 120
        controls = [
            "Controls:",
            "← → : Move",
            "↓ : Soft drop",
            "↑ : Rotate",
            "Click block: Info"
        ]
        
        for i, control in enumerate(controls):
            color = (255, 255, 255) if i == 0 else (200, 200, 200)
            control_text = self.small_font.render(control, True, color)
            self.screen.blit(control_text, (20, controls_y + i * 20))
    
    def wrap_text(self, text: str, max_width: int) -> List[str]:
        """Wrap text to fit within max_width pixels"""
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + (" " if current_line else "") + word
            if self.small_font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def handle_click(self, pos: Tuple[int, int]):
        """Handle mouse click for component selection"""
        grid_x, grid_y = pos[0] - GRID_X, pos[1] - GRID_Y
        
        if 0 <= grid_x < GRID_WIDTH * BLOCK_SIZE and 0 <= grid_y < GRID_HEIGHT * BLOCK_SIZE:
            cell_x = grid_x // BLOCK_SIZE
            cell_y = grid_y // BLOCK_SIZE
            
            if 0 <= cell_x < GRID_WIDTH and 0 <= cell_y < GRID_HEIGHT:
                block = self.grid[cell_y][cell_x]
                if block:
                    self.selected_component = block.component_type
    
    def update(self, dt: int):
        """Update game state"""
        if not self.current_block:
            return
            
        self.fall_time += dt
        if self.fall_time >= self.fall_speed:
            if self.can_move(0, 1):
                self.current_block.y += 1
            else:
                self.place_block()
            self.fall_time = 0
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            dt = self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if self.current_block:
                        if event.key == pygame.K_LEFT and self.can_move(-1, 0):
                            self.current_block.x -= 1
                        elif event.key == pygame.K_RIGHT and self.can_move(1, 0):
                            self.current_block.x += 1
                        elif event.key == pygame.K_DOWN and self.can_move(0, 1):
                            self.current_block.y += 1
                            self.score += 1
                        elif event.key == pygame.K_UP:
                            rotated = self.rotate_shape(self.current_block.shape)
                            if self.can_move(0, 0, rotated):
                                self.current_block.shape = rotated
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            
            self.update(dt)
            
            # Draw everything
            self.draw_gradient_background()
            self.draw_grid()
            self.draw_placed_blocks()
            
            if self.current_block:
                self.draw_block(self.current_block)
            
            self.draw_ui()
            
            pygame.display.flip()
        
        pygame.quit()

if __name__ == "__main__":
    game = CommonGroundGame()
    game.run()
