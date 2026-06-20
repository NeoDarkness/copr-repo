Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch
BuildRequires:  unzip

%global base_url %{url}/releases/download/v%{version}
%global iconsdir %{_datadir}/icons

Source0:        %{base_url}/catppuccin-frappe-blue-cursors.zip
Source1:        %{base_url}/catppuccin-frappe-dark-cursors.zip
Source2:        %{base_url}/catppuccin-frappe-flamingo-cursors.zip
Source3:        %{base_url}/catppuccin-frappe-green-cursors.zip
Source4:        %{base_url}/catppuccin-frappe-lavender-cursors.zip
Source5:        %{base_url}/catppuccin-frappe-light-cursors.zip
Source6:        %{base_url}/catppuccin-frappe-maroon-cursors.zip
Source7:        %{base_url}/catppuccin-frappe-mauve-cursors.zip
Source8:        %{base_url}/catppuccin-frappe-peach-cursors.zip
Source9:        %{base_url}/catppuccin-frappe-pink-cursors.zip
Source10:       %{base_url}/catppuccin-frappe-red-cursors.zip
Source11:       %{base_url}/catppuccin-frappe-rosewater-cursors.zip
Source12:       %{base_url}/catppuccin-frappe-sapphire-cursors.zip
Source13:       %{base_url}/catppuccin-frappe-sky-cursors.zip
Source14:       %{base_url}/catppuccin-frappe-teal-cursors.zip
Source15:       %{base_url}/catppuccin-frappe-yellow-cursors.zip

Source16:       %{base_url}/catppuccin-latte-blue-cursors.zip
Source17:       %{base_url}/catppuccin-latte-dark-cursors.zip
Source18:       %{base_url}/catppuccin-latte-flamingo-cursors.zip
Source19:       %{base_url}/catppuccin-latte-green-cursors.zip
Source20:       %{base_url}/catppuccin-latte-lavender-cursors.zip
Source21:       %{base_url}/catppuccin-latte-light-cursors.zip
Source22:       %{base_url}/catppuccin-latte-maroon-cursors.zip
Source23:       %{base_url}/catppuccin-latte-mauve-cursors.zip
Source24:       %{base_url}/catppuccin-latte-peach-cursors.zip
Source25:       %{base_url}/catppuccin-latte-pink-cursors.zip
Source26:       %{base_url}/catppuccin-latte-red-cursors.zip
Source27:       %{base_url}/catppuccin-latte-rosewater-cursors.zip
Source28:       %{base_url}/catppuccin-latte-sapphire-cursors.zip
Source29:       %{base_url}/catppuccin-latte-sky-cursors.zip
Source30:       %{base_url}/catppuccin-latte-teal-cursors.zip
Source31:       %{base_url}/catppuccin-latte-yellow-cursors.zip

Source32:       %{base_url}/catppuccin-macchiato-blue-cursors.zip
Source33:       %{base_url}/catppuccin-macchiato-dark-cursors.zip
Source34:       %{base_url}/catppuccin-macchiato-flamingo-cursors.zip
Source35:       %{base_url}/catppuccin-macchiato-green-cursors.zip
Source36:       %{base_url}/catppuccin-macchiato-lavender-cursors.zip
Source37:       %{base_url}/catppuccin-macchiato-light-cursors.zip
Source38:       %{base_url}/catppuccin-macchiato-maroon-cursors.zip
Source39:       %{base_url}/catppuccin-macchiato-mauve-cursors.zip
Source40:       %{base_url}/catppuccin-macchiato-peach-cursors.zip
Source41:       %{base_url}/catppuccin-macchiato-pink-cursors.zip
Source42:       %{base_url}/catppuccin-macchiato-red-cursors.zip
Source43:       %{base_url}/catppuccin-macchiato-rosewater-cursors.zip
Source44:       %{base_url}/catppuccin-macchiato-sapphire-cursors.zip
Source45:       %{base_url}/catppuccin-macchiato-sky-cursors.zip
Source46:       %{base_url}/catppuccin-macchiato-teal-cursors.zip
Source47:       %{base_url}/catppuccin-macchiato-yellow-cursors.zip

Source48:       %{base_url}/catppuccin-mocha-blue-cursors.zip
Source49:       %{base_url}/catppuccin-mocha-dark-cursors.zip
Source50:       %{base_url}/catppuccin-mocha-flamingo-cursors.zip
Source51:       %{base_url}/catppuccin-mocha-green-cursors.zip
Source52:       %{base_url}/catppuccin-mocha-lavender-cursors.zip
Source53:       %{base_url}/catppuccin-mocha-light-cursors.zip
Source54:       %{base_url}/catppuccin-mocha-maroon-cursors.zip
Source55:       %{base_url}/catppuccin-mocha-mauve-cursors.zip
Source56:       %{base_url}/catppuccin-mocha-peach-cursors.zip
Source57:       %{base_url}/catppuccin-mocha-pink-cursors.zip
Source58:       %{base_url}/catppuccin-mocha-red-cursors.zip
Source59:       %{base_url}/catppuccin-mocha-rosewater-cursors.zip
Source60:       %{base_url}/catppuccin-mocha-sapphire-cursors.zip
Source61:       %{base_url}/catppuccin-mocha-sky-cursors.zip
Source62:       %{base_url}/catppuccin-mocha-teal-cursors.zip
Source63:       %{base_url}/catppuccin-mocha-yellow-cursors.zip

%description
Catppuccin cursor themes (Frappé, Latte, Macchiato, Mocha).

%prep
%autosetup -T -c

for archive in %{_sourcedir}/catppuccin-*-cursors.zip; do
    unzip -q "$archive"
done

%install
install -d %{buildroot}%{iconsdir}

cp -pr catppuccin-*-cursors %{buildroot}%{iconsdir}/

%files
%{iconsdir}/catppuccin-*-cursors/

%changelog
%autochangelog