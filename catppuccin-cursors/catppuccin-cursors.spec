Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch

BuildRequires:  unzip
Requires:       catppuccin-frappe-cursors     = %{version}-%{release}
Requires:       catppuccin-latte-cursors      = %{version}-%{release}
Requires:       catppuccin-macchiato-cursors  = %{version}-%{release}
Requires:       catppuccin-mocha-cursors      = %{version}-%{release}

%global base_url https://github.com/catppuccin/cursors/releases/download/v%{version}

%global flavors \
    frappe \
    latte \
    macchiato \
    mocha

%global accents \
    blue \
    dark \
    flamingo \
    green \
    lavender \
    light \
    maroon \
    mauve \
    peach \
    pink \
    red \
    rosewater \
    sapphire \
    sky \
    teal \
    yellow

%global source_index 0

%foreach flavor in %{flavors}
%foreach accent in %{accents}
Source%{source_index}: %{base_url}/catppuccin-%{flavor}-%{accent}-cursors.zip
%global source_index %(expr %{source_index} + 1)
%endforeach
%endforeach

%description
Meta package for all Catppuccin cursor themes.

%package -n catppuccin-frappe-cursors
Summary:        Catppuccin Frappé cursor themes

%description -n catppuccin-frappe-cursors
Catppuccin Frappé cursor themes in all accent colors.

%package -n catppuccin-latte-cursors
Summary:        Catppuccin Latte cursor themes

%description -n catppuccin-latte-cursors
Catppuccin Latte cursor themes in all accent colors.

%package -n catppuccin-macchiato-cursors
Summary:        Catppuccin Macchiato cursor themes

%description -n catppuccin-macchiato-cursors
Catppuccin Macchiato cursor themes in all accent colors.

%package -n catppuccin-mocha-cursors
Summary:        Catppuccin Mocha cursor themes

%description -n catppuccin-mocha-cursors
Catppuccin Mocha cursor themes in all accent colors.

%prep
%setup -q -T -c -n %{name}-%{version}

for archive in %{_sourcedir}/catppuccin-*-cursors.zip; do
    unzip -q "${archive}"
done

%install
install -d %{buildroot}%{_datadir}/icons

for dir in catppuccin-*-cursors; do
    cp -a "${dir}" %{buildroot}%{_datadir}/icons/
done

# Remove duplicated metadata files from installed directories
find %{buildroot}%{_datadir}/icons/catppuccin-*-cursors \
    -maxdepth 1 \
    \( -name LICENSE -o -name AUTHORS \) \
    -delete

%files

%files -n catppuccin-frappe-cursors
%license catppuccin-frappe-blue-cursors/LICENSE
%doc catppuccin-frappe-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-frappe-*-cursors/

%files -n catppuccin-latte-cursors
%license catppuccin-latte-blue-cursors/LICENSE
%doc catppuccin-latte-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-latte-*-cursors/

%files -n catppuccin-macchiato-cursors
%license catppuccin-macchiato-blue-cursors/LICENSE
%doc catppuccin-macchiato-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-macchiato-*-cursors/

%files -n catppuccin-mocha-cursors
%license catppuccin-mocha-blue-cursors/LICENSE
%doc catppuccin-mocha-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-mocha-*-cursors/

%changelog
%autochangelog
