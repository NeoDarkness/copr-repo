%global forgeurl https://github.com/catppuccin/cursors

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-2.0-only

%forgemeta

URL:            https://github.com/catppuccin/cursors
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-pyside6
BuildRequires:  catppuccin-whiskers
BuildRequires:  xcursorgen
BuildRequires:  inkscape
BuildRequires:  just

Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package that installs all Catppuccin cursor themes:
Latte, Frappe, Macchiato, and Mocha.

%package latte
Summary:        Catppuccin Latte cursor theme

%description latte
Catppuccin Latte flavor cursor theme.

%package frappe
Summary:        Catppuccin Frappe cursor theme

%description frappe
Catppuccin Frappe flavor cursor theme.

%package macchiato
Summary:        Catppuccin Macchiato cursor theme

%description macchiato
Catppuccin Macchiato flavor cursor theme.

%package mocha
Summary:        Catppuccin Mocha cursor theme

%description mocha
Catppuccin Mocha flavor cursor theme.

%prep
%forgeautosetup

%build
just all

%install
install -d %{buildroot}%{_datadir}/icons
cp -a dist/* %{buildroot}%{_datadir}/icons/

find %{buildroot}%{_datadir}/icons/ \
    \( -name "LICENSE" -o -name "AUTHORS" -o -name "manifest.hl" \) \
    -delete

for dir in %{buildroot}%{_datadir}/icons/catppuccin-*-cursors; do
    /bin/touch "$dir/icon-theme.cache"
done

%post latte
for dir in %{_datadir}/icons/catppuccin-latte-*-cursors; do
    /bin/touch --no-create "$dir" &>/dev/null || :
done

%post frappe
for dir in %{_datadir}/icons/catppuccin-frappe-*-cursors; do
    /bin/touch --no-create "$dir" &>/dev/null || :
done

%post macchiato
for dir in %{_datadir}/icons/catppuccin-macchiato-*-cursors; do
    /bin/touch --no-create "$dir" &>/dev/null || :
done

%post mocha
for dir in %{_datadir}/icons/catppuccin-mocha-*-cursors; do
    /bin/touch --no-create "$dir" &>/dev/null || :
done

%postun latte
if [ $1 -eq 0 ]; then
    for dir in %{_datadir}/icons/catppuccin-latte-*-cursors; do
        /bin/touch --no-create "$dir" &>/dev/null
        /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
    done
fi

%postun frappe
if [ $1 -eq 0 ]; then
    for dir in %{_datadir}/icons/catppuccin-frappe-*-cursors; do
        /bin/touch --no-create "$dir" &>/dev/null
        /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
    done
fi

%postun macchiato
if [ $1 -eq 0 ]; then
    for dir in %{_datadir}/icons/catppuccin-macchiato-*-cursors; do
        /bin/touch --no-create "$dir" &>/dev/null
        /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
    done
fi

%postun mocha
if [ $1 -eq 0 ]; then
    for dir in %{_datadir}/icons/catppuccin-mocha-*-cursors; do
        /bin/touch --no-create "$dir" &>/dev/null
        /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
    done
fi

%posttrans latte
for dir in %{_datadir}/icons/catppuccin-latte-*-cursors; do
    /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
done

%posttrans frappe
for dir in %{_datadir}/icons/catppuccin-frappe-*-cursors; do
    /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
done

%posttrans macchiato
for dir in %{_datadir}/icons/catppuccin-macchiato-*-cursors; do
    /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
done

%posttrans mocha
for dir in %{_datadir}/icons/catppuccin-mocha-*-cursors; do
    /usr/bin/gtk-update-icon-cache "$dir" &>/dev/null || :
done

%check
# No test suite available

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md 

%files latte
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%dir %{_datadir}/icons/catppuccin-latte-*-cursors
%{_datadir}/icons/catppuccin-latte-*-cursors/
%ghost %{_datadir}/icons/catppuccin-latte-*-cursors/icon-theme.cache

%files frappe
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%dir %{_datadir}/icons/catppuccin-frappe-*-cursors
%{_datadir}/icons/catppuccin-frappe-*-cursors/
%ghost %{_datadir}/icons/catppuccin-frappe-*-cursors/icon-theme.cache

%files macchiato
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%dir %{_datadir}/icons/catppuccin-macchiato-*-cursors
%{_datadir}/icons/catppuccin-macchiato-*-cursors/
%ghost %{_datadir}/icons/catppuccin-macchiato-*-cursors/icon-theme.cache

%files mocha
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%dir %{_datadir}/icons/catppuccin-mocha-*-cursors
%{_datadir}/icons/catppuccin-mocha-*-cursors/
%ghost %{_datadir}/icons/catppuccin-mocha-*-cursors/icon-theme.cache

%changelog
%autochangelog