-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

vim.opt.foldenable = false
vim.opt.foldmethod = "indent"
vim.api.nvim_set_hl(0, "AlphaHeader", { fg = "#61afef" })
vim.api.nvim_set_hl(0, "AlphaButtons", { fg = "#89ca78" })
vim.api.nvim_set_hl(0, "AlphaFooter", { fg = "#e5c07b" })
